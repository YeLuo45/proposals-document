# Technical Solution: React Native 安卓计算器

**Proposal ID**: P-20250416-003
**版本**: v1.0
**日期**: 2026-04-16
**Owner**: 小墨
**Status**: approved_for_dev

---

## 1. 技术栈决策

| 决策点 | 选择 | 理由 |
|--------|------|------|
| 框架 | React Native 0.76+ (CLI init) | boss 明确选择 CLI，非 Expo |
| 语言 | TypeScript | 类型安全，PRD 已明确 |
| 状态管理 | React Context + useReducer | 轻量，无额外依赖 |
| UI 组件库 | React Native Paper (MD3) | PRD 指定 MD3 风格 |
| 动画 | React Native Reanimated 3 | Paper 依赖项 |
| 数学表达式 | mathjs (^12.x) | boss 明确引入，自研不考核 |
| 单位转换 | 自研（数据驱动配置） | 固定规则，数据驱动最轻 |
| 汇率 API | frankfurter.app (free, no key) | boss 要求免费，frankfurter 完全免费无限制 |
| 本地存储 | @react-native-async-storage/async-storage | 汇率缓存 + 历史记录 |
| 构建 | Gradle (Android) + Metro | RN CLI 标准流程 |

---

## 2. 项目结构

```
calculator-app/
├── src/
│   ├── components/
│   │   ├── Button.tsx              # 计算器按键组件
│   │   ├── Display.tsx             # 显示区域组件
│   │   ├── ModeTab.tsx             # 模式切换标签栏
│   │   └── UnitConverter.tsx       # 单位转换面板
│   ├── screens/
│   │   └── CalculatorScreen.tsx   # 主屏（含三种模式）
│   ├── utils/
│   │   ├── calculator.ts          # mathjs 封装，计算核心
│   │   ├── formatter.ts           # 数字格式化（千分位/科学计数）
│   │   └── units.ts               # 单位转换数据 + 逻辑
│   ├── services/
│   │   └── exchangeRate.ts        # 汇率 API 服务（frankfurter.app）
│   ├── hooks/
│   │   ├── useCalculator.ts        # 计算器状态 hook
│   │   └── useExchangeRate.ts     # 汇率 hook（含缓存）
│   ├── context/
│   │   └── CalculatorContext.tsx  # 全局计算器状态
│   └── constants/
│       ├── theme.ts               # 主题色/布局常量
│       └── units.ts               # 单位数据
├── android/                        # Android 原生项目（CLI init产物）
├── App.tsx
└── index.js
```

---

## 3. 计算核心设计

### 3.1 mathjs 封装

```typescript
// utils/calculator.ts
import { evaluate, format } from 'mathjs';

export const calculate = (expression: string): string => {
  try {
    const result = evaluate(expression);
    return format(result, { precision: 14, notation: 'auto' });
  } catch {
    return 'Error';
  }
};

export const formatResult = (value: string): string => {
  // 处理显示：自动切换千分位 / 科学计数法
  // 长数字 > 12 位切科学计数
  // 短数字加千分位分隔符
};
```

### 3.2 表达式处理流程

```
用户输入 → 清洗表达式（去除空格、处理负号）→ mathjs evaluate → 格式化显示
```

- 连续运算符处理：`+-` → `+`，`×-` → `×-1`
- 百分比处理：`50%` → `0.5`
- 括号匹配校验

---

## 4. 汇率服务设计

### 4.1 API

- **Base URL**: `https://api.frankfurter.app`
- **Endpoints**:
  - `GET /latest?from=USD&to=CNY,EUR` — 获取最新汇率
  - **注意**: frankfurter 支持的货币有限（EUR为主），英镑/日元/韩元等可能不在支持列表
  - **Fallback**: 若货币不在支持列表，显示"该货币暂不支持"

### 4.2 缓存策略

```typescript
// 启动时获取汇率，写入 AsyncStorage
// key: '@exchange_rates', value: { rates: {...}, timestamp: Date }
// 缓存有效期: 24小时（避免每次启动都请求）
// 离线时使用过期缓存，UI 提示"汇率可能过期"
```

### 4.3 支持货币

- 人民币 CNY（frankfurter 不直接支持，间接计算）
- 美元 USD
- 欧元 EUR
- 英镑 GBP
- 日元 JPY（需 EUR 桥接）
- 韩元 KRW（需 EUR 桥接）
- 港币 HKD

---

## 5. 单位转换设计

### 5.1 数据结构

```typescript
// 每类单位一个转换基准值，查询时做比例换算
const LENGTH_UNITS = {
  meter: 1,
  centimeter: 0.01,
  millimeter: 0.001,
  inch: 0.0254,
  foot: 0.3048,
  yard: 0.9144,
  kilometer: 1000,
  mile: 1609.344,
};

const convert = (value: number, from: string, to: string, unitMap: Record<string, number>) => {
  const base = value * unitMap[from];
  return base / unitMap[to];
};
```

### 5.2 覆盖类别

| 类别 | 单位数 |
|------|--------|
| 长度 | 8 |
| 重量 | 6 |
| 温度 | 3（特殊处理，℃/℉/K） |
| 面积 | 6 |
| 体积 | 6 |
| 速度 | 4 |

---

## 6. UI 架构

### 6.1 主题色

```typescript
// constants/theme.ts
export const COLORS = {
  primary: '#4CAF50',
  primaryDark: '#388E3C',
  background: '#FAFAFA',
  surface: '#FFFFFF',
  buttonNumber: '#FFFFFF',
  buttonOperator: '#E8F5E9',
  buttonEquals: '#4CAF50',
  textPrimary: '#212121',
  textSecondary: '#757575',
};

export const DARK_COLORS = {
  primary: '#81C784',
  primaryDark: '#4CAF50',
  background: '#121212',
  surface: '#1E1E1E',
  buttonNumber: '#2D2D2D',
  buttonOperator: '#1B5E20',
  buttonEquals: '#4CAF50',
  textPrimary: '#FFFFFF',
  textSecondary: '#B0B0B0',
};
```

### 6.2 模式切换

```
ModeTab: [ 基础 | 科学 | 转换 ]
```

- 基础/科学模式：复用 Button + Display 组件，差异在按键布局
- 转换模式：切换为 UnitConverter 面板

### 6.3 按键布局

**基础模式（4×5）**: 同 PRD 规范
**科学模式（扩展 5×6）**: 基础 + 一行科学函数（sin/cos/tan/log/ln/√）
**转换模式**: 类别选择 + 两列输入 + 单位选择器

---

## 7. 包体积控制（< 30MB）

### 7.1 关键措施

| 措施 | 说明 |
|------|------|
| mathjs 按需引入 | ES tree-shaking，只用 `evaluate` + `format` |
| 无图片资源 | 全部用 Unicode 字符 + vector icon |
| React Native Paper | 只导入用到的组件（Button, Text, Icon, SegmentedButtons） |
| 移除 Hermes（可选） | 对计算器无必要，但可能影响兼容性，暂不调整 |
| Debug APK vs Release APK | Debug APK 含 JS bundle ~15MB，Release 优化后更小 |

### 7.2 预期包体积

| 产物 | 预期大小 |
|------|----------|
| app-debug.apk (with JS bundle) | ~20-25MB |
| app-release.apk (AAB for Play Store) | ~12-18MB |

---

## 8. 构建与交付

### 8.1 构建命令

```bash
# Debug APK（含 JS bundle，可独立运行）
cd calculator-app
npx react-native build-android --mode debug

# 或
cd android && ./gradlew assembleDebug

# 输出: android/app/build/outputs/apk/debug/app-debug.apk
```

### 8.2 交付物

- `app-debug.apk` — 可直接安装到 Android 7.0+ 设备的 APK
- 源码目录 `calculator-app/`
- 构建说明文档

---

## 9. 关键风险与缓解

| 风险 | 缓解方案 |
|------|----------|
| frankfurter 不支持 CNY/KRW/JPY 直接换算 | 通过 EUR 桥接（CNY→EUR→USD），间接计算 |
| mathjs 精度问题 | 使用 `format(..., { precision: 14 })` 统一保留14位有效数字 |
| 包体积超30MB | 优先移除不必要的 Paper 组件，tree-shaking 确认 |
| 深色模式适配遗漏 | Paper 默认支持，验证时测试两种模式 |

---

## 10. Dev 交付标准

- [ ] `npx react-native init calculator-app` 成功，Android 构建通过
- [ ] mathjs 表达式求值正确（基础运算 + 科学函数）
- [ ] 单位转换6类全覆盖
- [ ] 汇率 API 调用成功（frankfurter），缓存机制正常
- [ ] 浅色/深色模式正常
- [ ] `assembleDebug` 成功，APK < 30MB
- [ ] 核心功能自测截图
