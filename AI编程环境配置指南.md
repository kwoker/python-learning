# AI编程环境配置完整指南

> 🎯 本指南详细说明如何搭建 AI 编程环境，使用 Claude Code 进行智能编程

## 📋 目录

- [前置准备](#前置准备)
- [开发工具安装](#开发工具安装)
- [环境配置](#环境配置)
- [VS Code 插件配置](#vs-code-插件配置)
- [验证配置](#验证配置)
- [常见问题](#常见问题)
- [故障排除](#故障排除)

---

## 🎯 前置准备

### 1. 订阅 MiniMax Coding Plan

在开始之前，你需要先订阅 MiniMax 的 Coding Plan 服务：

- 📝 **访问链接**: [MiniMax Coding Plan](https://platform.minimaxi.com/docs/coding-plan/intro)
- 💳 **充值方式**: 根据页面指引完成充值
- 🔑 **生成 API Key**: 充值后生成你的专属 API Key

> ⚠️ **重要**: API Key 是后续配置的关键，请妥善保管

### 2. 开发环境要求

| 工具 | 版本要求 | 说明 |
|------|----------|------|
| Node.js | 最新稳定版 | [nodejs.org](https://nodejs.org/) 下载 |
| Python | 3.8+ | 必需，建议 3.9+ |
| VS Code | 最新版 | 代码编辑器 |

---

## 🛠️ 开发工具安装

### 步骤 1: 安装 Node.js 和 Python

#### Windows 用户
1. 访问 [nodejs.org](https://nodejs.org/) 下载并安装 Node.js
2. 访问 [python.org](https://www.python.org/) 下载并安装 Python 3.8+
3. 安装时勾选 "Add Python to PATH"

#### macOS 用户
推荐使用自动化脚本安装：

```bash
# 安装基础环境（包含 Node.js, Python 等）
curl -fsSL https://dotfiles.keveon.io/install.sh | bash

# 可选参数
# --ssh : 使用 SSH
# --force : 强制重新安装
```

**手动安装**:
```bash
# 安装 Homebrew（如果尚未安装）
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 安装 Node.js
brew install node

# 安装 Python
brew install python
```

#### Linux 用户
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install nodejs npm python3 python3-pip

# CentOS/RHEL
sudo yum install nodejs npm python3 python3-pip
```

### 步骤 2: 安装 pnpm

以**管理员权限**运行终端/命令提示符，执行：

```bash
# 全局安装 pnpm
npm i -g pnpm

# 初始化 pnpm
pnpm setup
```

### 步骤 3: 安装 Claude Code

```bash
# 安装 Claude Code CLI 工具
pnpm install -g @anthropic-ai/claude-code
```

---

## ⚙️ 环境配置

### 步骤 1: 配置 CLAUDE.md

1. **下载配置文件**
   - 访问: [reliable-coding-agent](https://github.com/Swfdong/reliable-coding-agent)
   - 下载项目中的 `CLAUDE.md` 文件

2. **放置配置文件**
   - **Windows**: `C:\users\你的用户名\.claude\CLAUDE.md`
   - **macOS**: `~/.claude/CLAUDE.md`
   - **Linux**: `~/.claude/CLAUDE.md`

### 步骤 2: 配置 API Key

1. **访问快速开始文档**: [MiniMax Quickstart](https://platform.minimaxi.com/docs/coding-plan/quickstart)

2. **按照步骤 1-3 操作**:
   - 步骤 1: 创建配置文件
   - 步骤 2: 填写 API Key
   - 步骤 3: 保存配置

3. **使用 Claude Code 创建配置**:
   - 打开 Claude Code
   - 创建新文件
   - 粘贴 JSON 配置内容
   - 填入你的 API Key

### 步骤 3: 验证安装

检查 Claude Code 是否正确安装：

```bash
# 检查版本
claude --version

# 或
claude-code --version
```

---

## 🔌 VS Code 插件配置

### 安装 Claude Code 插件

1. **打开 VS Code**
2. **进入扩展商店** (Ctrl+Shift+X)
3. **搜索 "Claude Code"**
4. **点击安装**

### 插件设置

安装完成后，点击插件旁边的 ⚙️ **设置图标**，进行以下配置：

#### ✅ 必须启用的选项

| 选项 | 状态 | 说明 |
|------|------|------|
| `Allow Bypass` | ✅ 启用 | 提供超级权限，允许执行高权限操作 |
| `Disable Login` | ✅ 启用 | 禁用登录（使用 API Key 验证） |

#### 📝 选项说明

- **Bypass (绕过)**:
  - 提供超级权限
  - 可以执行更高级的操作
  - 建议在受信任的环境中使用

- **Plan Mode (规划模式)**:
  - 先制定计划，再执行
  - 适合复杂任务
  - 避免意外操作
  - **推荐日常使用**

---

## ✅ 验证配置

### 检查清单

完成配置后，验证以下项目：

- [ ] MiniMax Coding Plan 已订阅并充值
- [ ] API Key 已生成并配置
- [ ] Node.js 已安装 (`node --version`)
- [ ] Python 已安装 (`python --version`)
- [ ] pnpm 已安装 (`pnpm --version`)
- [ ] Claude Code 已安装 (`claude --version`)
- [ ] VS Code 插件已安装
- [ ] 插件设置已配置
- [ ] CLAUDE.md 已放置在正确位置

### 快速测试

1. **在 VS Code 中**:
   - 打开任意项目
   - 打开命令面板 (Ctrl+Shift+P)
   - 输入 "Claude Code"
   - 如果能正常显示命令，说明配置成功

2. **测试 AI 交互**:
   - 创建一个新文件
   - 向 Claude Code 提问（如："帮我写一个 Hello World 程序"）
   - 检查是否能正常响应

---

## ❓ 常见问题

### Q1: 提示 "command not found" 错误

**解决方案**:
```bash
# 重新安装 pnpm
npm uninstall -g pnpm
npm install -g pnpm

# 重新运行 setup
pnpm setup

# 重启终端
```

### Q2: API Key 无效

**检查项目**:
- API Key 是否正确复制（无多余空格）
- Coding Plan 是否已充值
- 网络连接是否正常

### Q3: VS Code 插件无法连接

**解决方案**:
1. 重启 VS Code
2. 检查插件设置
3. 重新安装插件

### Q4: macOS 自动化脚本安装失败

**解决方案**:
```bash
# 手动安装
brew install node python

# 或下载安装包
# Node.js: https://nodejs.org/
# Python: https://www.python.org/downloads/
```

### Q5: 权限不足错误

**解决方案**:
- Windows: 以管理员身份运行命令提示符
- macOS/Linux: 使用 `sudo`
- 或者使用 `sudo pnpm install -g @anthropic-ai/claude-code`

---

## 🚨 故障排除

### 步骤 1: 检查系统要求

确保你的系统满足最低要求：
- **Windows**: Windows 10 或更高版本
- **macOS**: macOS 10.15 或更高版本
- **Linux**: Ubuntu 18.04+ / CentOS 7+

### 步骤 2: 重新安装

如果遇到问题，可以尝试完全重新安装：

```bash
# 1. 卸载旧版本
npm uninstall -g @anthropic-ai/claude-code
npm uninstall -g pnpm

# 2. 清理缓存
npm cache clean --force

# 3. 重新安装
npm i -g pnpm
pnpm setup
pnpm install -g @anthropic-ai/claude-code
```

### 步骤 3: 查看日志

如果问题仍然存在，查看详细日志：

```bash
# 启用详细输出
claude --verbose

# 或查看错误日志
claude --debug
```

### 步骤 4: 联系支持

如果无法解决：
- 📧 发送邮件给 MiniMax 支持
- 💬 加入官方社区讨论
- 📝 在 GitHub 上提交 Issue

---

## 📚 相关资源

- [MiniMax 官方文档](https://platform.minimaxi.com/docs/)
- [Claude Code 官方仓库](https://github.com/anthropics/claude-code)
- [reliable-coding-agent](https://github.com/Swfdong/reliable-coding-agent)
- [VS Code 官网](https://code.visualstudio.com/)

---

## 🎉 完成

恭喜！你已经成功搭建了 AI 编程环境。现在可以：

1. 🚀 启动 VS Code
2. 🤖 打开 Claude Code
3. 💻 开始你的 AI 编程之旅！

> 💡 **提示**: 建议使用 Plan Mode 进行复杂任务，可以先让 AI 制定计划，再确认执行。

---

**版本**: v1.0
**最后更新**: 2024-12-17
