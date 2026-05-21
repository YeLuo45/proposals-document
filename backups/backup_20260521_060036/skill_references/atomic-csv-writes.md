# Atomic CSV Write Mechanism (v3.3.0)

> 2026-05-21 新增：`proposal_manager_cli.py` 的 `write_csv()` 改为原子写入，防止 CSV 文件损坏。

## 问题背景

原始 `write_csv()` 直接用 `open(path, 'w')` 覆盖写入：
- 写入过程中进程崩溃 → CSV 文件可能只有部分数据
- 没有任何备份 → 损坏后无法恢复
- 没有操作日志 → 无法诊断何时/谁修改了 CSV

## 解决方案：三文件原子写入

```
write_csv(path, headers, rows):
  1. 写入 path.tmp（临时文件）
  2. 复制 path → path.bak（备份旧版本）
  3. rename path.tmp → path（原子替换）
  4. 追加 audit.log 审计记录
```

## 为什么安全

1. **原子性**：Linux 同文件系统的 `rename()` 是原子操作，不会出现"写了一半"的文件
2. **可恢复**：`.bak` 保留修改前的完整版本，出问题可手动恢复
3. **可审计**：`audit.log` 记录每次 CSV 写入的时间戳、文件名、行数、字段数

## 审计日志格式

```
[2026-05-21 01:30:45] CSV_WRITE | proposals.csv | 228 rows, 22 fields
[2026-05-21 01:31:12] CSV_WRITE | projects.csv | 69 rows, 7 fields
[2026-05-21 01:32:00] ERROR | die | Project does not exist: PRJ-20990101-999
```

## execute_code 执行 Python 时文件截断陷阱

**症状**：proposals.csv 被清空为 1 行（只有 header）。

**根因**：Python execute_code 的 `open('/path/to/file', 'w')` 在执行前就截断文件。如果代码在 `f.write()` 之前报错（缩进错误/语法错误/进程中断），整个文件被清空。

```python
# ❌ 危险：文件在 write() 调用的 Python 进程启动时就已被截断
with open('/home/hermes/proposals/proposals.csv', 'w') as f:
    # 如果这里报错（缩进错误等），文件已经被截断为 0 字节
    f.write(content)

# ✅ 安全：使用 proposal_manager_cli.py 的 add/update 命令
# 或先读取再写入（但 execute_code 中不推荐用 open() 模式）
```

**重要**：execute_code 工具运行在独立的 Python 进程中，与 terminal 的 git 工作目录无共享状态。即使 terminal 执行了 `git checkout -- proposals.csv`，execute_code 进程的 open() 仍会截断文件。

**预防**：
1. 始终使用 `proposal_manager_cli.py` 的 `proposal add/update` 命令修改 proposals.csv
2. 不要用 execute_code 直接读写 CSV 文件
3. 如果 CSV 损坏，从 git 恢复：`git checkout -- proposals.csv`

## 恢复步骤

如果 CSV 文件损坏：

如果 CSV 文件损坏：
```bash
cd /home/hermes/proposals

# 方法1：从 .bak 恢复
cp proposals.csv.bak proposals.csv

# 方法2：从 Git 恢复（如果 proposals/ 是 git 仓库）
git checkout -- proposals.csv

# 方法3：从备份恢复
cp backups/backup_YYYYMMDD_HHMMSS/proposals.csv proposals.csv
```

## 验证

```bash
# 检查 CSV 行数
wc -l /home/hermes/proposals/proposals.csv
wc -l /home/hermes/proposals/projects.csv

# 查看最近审计记录
tail -5 /home/hermes/proposals/audit.log

# 确认 .tmp 没有残留
ls /home/hermes/proposals/*.tmp 2>/dev/null && echo "WARNING: .tmp残留" || echo "OK: 无残留"
```
