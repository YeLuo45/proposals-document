#!/bin/bash
# check-persona-docs.sh — Verify USER.md/SOUL.md/MEMORY.md compliance
# Usage: bash check-persona-docs.sh [--json] [--profile <name>]
#   --profile onepc  → check /home/hermes/.hermes/profiles/onepc/ persona docs
#   (default)        → check main /home/hermes/.hermes/ persona docs
# Exit code: 0 = all pass, 1 = violations found

set -euo pipefail

PROFILE=""
OUTPUT_JSON=false
while [[ $# -gt 0 ]]; do
    case "$1" in
        --json) OUTPUT_JSON=true; shift ;;
        --profile) PROFILE="$2"; shift 2 ;;
        *) shift ;;
    esac
done

TEMPLATES_DIR="${TEMPLATES_DIR:-/home/hermes/proposals/templates}"

if [[ -n "$PROFILE" ]]; then
    PROFILE_ROOT="/home/hermes/.hermes/profiles/$PROFILE"
    MEMORIES_DIR="$PROFILE_ROOT/memories"
    SOUL_PATH="$PROFILE_ROOT/SOUL.md"
else
    MEMORIES_DIR="${MEMORIES_DIR:-/home/hermes/.hermes/memories}"
    SOUL_PATH="${SOUL_PATH:-/home/hermes/.hermes/SOUL.md}"
fi

PASS=0
FAIL=0
RESULTS=()

check_file() {
    local label="$1" path="$2" min_lines="$3"
    if [[ -f "$path" ]]; then
        local lines
        lines=$(wc -l < "$path")
        if [[ "$lines" -ge "$min_lines" ]]; then
            RESULTS+=("✅ $label: $lines lines")
            ((PASS++))
        else
            RESULTS+=("❌ $label: $lines lines (expected ≥$min_lines)")
            ((FAIL++))
        fi
    else
        RESULTS+=("❌ $label: MISSING")
        ((FAIL++))
    fi
}

check_keyword() {
    local label="$1" path="$2" keyword="$3"
    if grep -q "$keyword" "$path" 2>/dev/null; then
        RESULTS+=("  ✅ $label: '$keyword' found")
        ((PASS++))
    else
        RESULTS+=("  ❌ $label: '$keyword' MISSING")
        ((FAIL++))
    fi
}

# === SOUL.md ===
check_file "SOUL.md" "$SOUL_PATH" 100
if [[ -f "$SOUL_PATH" ]]; then
    check_keyword "身份定义" "$SOUL_PATH" "CLI AI Agent"
    check_keyword "迭代偏好对比" "$SOUL_PATH" "迭代偏好对比"
    check_keyword "Test流程" "$SOUL_PATH" "测试用例"
    check_keyword "更新日志" "$SOUL_PATH" "更新日志"
    check_keyword "正确路径" "$SOUL_PATH" "/home/hermes/proposals"
    # Must NOT have old path
    if grep -q '~/.hermes/proposals' "$SOUL_PATH" 2>/dev/null; then
        RESULTS+=("  ❌ 旧路径残留: ~/.hermes/proposals found")
        ((FAIL++))
    else
        RESULTS+=("  ✅ 无旧路径残留")
        ((PASS++))
    fi
fi

# === USER.md ===
check_file "USER.md" "$MEMORIES_DIR/USER.md" 30
if [[ -f "$MEMORIES_DIR/USER.md" ]]; then
    check_keyword "基本信息" "$MEMORIES_DIR/USER.md" "## 基本信息"
    check_keyword "时区" "$MEMORIES_DIR/USER.md" "时区"
    check_keyword "GitHub偏好" "$MEMORIES_DIR/USER.md" "## GitHub 偏好"
    check_keyword "验证方式" "$MEMORIES_DIR/USER.md" "git ls-remote"
    check_keyword "更新日志" "$MEMORIES_DIR/USER.md" "## 更新日志"
    check_keyword "工作流偏好" "$MEMORIES_DIR/USER.md" "## 工作流偏好"
fi

# === MEMORY.md ===
check_file "MEMORY.md" "$MEMORIES_DIR/MEMORY.md" 50
if [[ -f "$MEMORIES_DIR/MEMORY.md" ]]; then
    check_keyword "记忆分层" "$MEMORIES_DIR/MEMORY.md" "记忆分层架构"
    check_keyword "存储策略" "$MEMORIES_DIR/MEMORY.md" "## 存储策略"
    check_keyword "触发条件" "$MEMORIES_DIR/MEMORY.md" "## 更新触发条件"
    check_keyword "技术决策" "$MEMORIES_DIR/MEMORY.md" "## 技术决策底线"
    check_keyword "已知坑点" "$MEMORIES_DIR/MEMORY.md" "## 已知坑点"
    check_keyword "更新日志" "$MEMORIES_DIR/MEMORY.md" "## 更新日志"
fi

# === Templates ===
check_file "SOUL.md (templates)" "$TEMPLATES_DIR/SOUL.md" 30
check_file "USER.md (templates)" "$TEMPLATES_DIR/USER.md" 30
check_file "MEMORY.md (templates)" "$TEMPLATES_DIR/MEMORY.md" 50

# === memory/ directory ===
if [[ -d "/home/hermes/proposals/memory/" ]]; then
    RESULTS+=("✅ memory/ directory exists")
    ((PASS++))
else
    RESULTS+=("❌ memory/ directory MISSING")
    ((FAIL++))
fi

# Output
if $OUTPUT_JSON; then
    echo "{\"pass\": $PASS, \"fail\": $FAIL, \"total\": $((PASS + FAIL))}"
else
    for r in "${RESULTS[@]}"; do
        echo "$r"
    done
    echo "---"
    echo "Pass: $PASS, Fail: $FAIL, Total: $((PASS + FAIL))"
fi

exit $(( FAIL > 0 ? 1 : 0 ))
