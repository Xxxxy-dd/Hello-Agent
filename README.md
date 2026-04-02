# Hello-Agent

Hello Agent 的入门实例代码 — A simple introductory AI Agent example.

## 简介 / Introduction

本项目演示了一个最简单的 Agent 模式：  
This project demonstrates a minimal Agent pattern:

1. **感知（Perceive）**：接收用户指令 / Receive user instruction  
2. **决策（Decide）**：选择合适的工具 / Select the right tool  
3. **行动（Act）**：执行工具并返回结果 / Execute the tool and return the result

## 快速开始 / Quick Start

```bash
python hello_agent.py
```

## 示例输出 / Sample Output

```
==================================================
       Hello Agent — 入门示例
==================================================
可用工具 / Available tools:
  - get_weather(city): 获取指定城市的天气 / Get weather for a city
  - calculate(expression): 计算数学表达式 / Calculate a math expression
  - say_hello(name): 向用户打招呼 / Say hello to the user

[say_hello(name='世界')]
  => 你好，世界！欢迎使用 Hello Agent！

[get_weather(city='北京')]
  => 晴天，气温 20°C

[calculate(expression='3 * (4 + 5)')]
  => 27

[get_weather(city='深圳')]
  => 抱歉，暂无 深圳 的天气信息。
```

## 项目结构 / Project Structure

```
Hello-Agent/
├── hello_agent.py   # 核心 Agent 代码 / Core agent code
└── README.md
```
