"""
Hello Agent - 入门示例代码
A simple introductory example demonstrating a basic AI agent pattern.
"""

import ast
import operator


# 工具定义 / Tool definitions
def get_weather(city: str) -> str:
    """模拟获取天气信息 / Simulate fetching weather info."""
    weather_data = {
        "北京": "晴天，气温 20°C",
        "上海": "多云，气温 18°C",
        "广州": "小雨，气温 25°C",
    }
    return weather_data.get(city, f"抱歉，暂无 {city} 的天气信息。")


# Supported operators for safe expression evaluation
_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}

_MAX_EXPR_LEN = 100


def _eval_node(node: ast.AST) -> float:
    """Recursively evaluate an AST node using only safe numeric operations."""
    if isinstance(node, ast.Expression):
        return _eval_node(node.body)
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in _OPERATORS:
        return _OPERATORS[type(node.op)](_eval_node(node.left), _eval_node(node.right))
    if isinstance(node, ast.UnaryOp) and type(node.op) in _OPERATORS:
        return _OPERATORS[type(node.op)](_eval_node(node.operand))
    raise ValueError(f"不支持的表达式节点：{type(node).__name__}")


def calculate(expression: str) -> str:
    """安全地计算数学表达式 / Safely evaluate a math expression."""
    if len(expression) > _MAX_EXPR_LEN:
        return f"错误：表达式过长（最多 {_MAX_EXPR_LEN} 个字符）。"
    try:
        tree = ast.parse(expression.strip(), mode="eval")
        result = _eval_node(tree)
        return str(result)
    except (ValueError, ZeroDivisionError, SyntaxError) as e:
        return f"计算出错：{e}"


def say_hello(name: str) -> str:
    """向用户打招呼 / Greet the user."""
    return f"你好，{name}！欢迎使用 Hello Agent！"


# 工具注册表 / Tool registry
TOOLS = {
    "get_weather": {
        "func": get_weather,
        "description": "获取指定城市的天气 / Get weather for a city",
        "params": ["city"],
    },
    "calculate": {
        "func": calculate,
        "description": "计算数学表达式 / Calculate a math expression",
        "params": ["expression"],
    },
    "say_hello": {
        "func": say_hello,
        "description": "向用户打招呼 / Say hello to the user",
        "params": ["name"],
    },
}


class HelloAgent:
    """
    一个简单的入门级 Agent。
    A simple introductory Agent that perceives input, selects a tool, and acts.
    """

    def __init__(self):
        self.tools = TOOLS

    def list_tools(self) -> str:
        lines = ["可用工具 / Available tools:"]
        for name, info in self.tools.items():
            params = ", ".join(info["params"])
            lines.append(f"  - {name}({params}): {info['description']}")
        return "\n".join(lines)

    def run(self, tool_name: str, **kwargs) -> str:
        """
        执行指定工具并返回结果。
        Execute the specified tool and return its result.
        """
        if tool_name not in self.tools:
            available = ", ".join(self.tools.keys())
            return f"未知工具 '{tool_name}'。可用工具：{available}"
        tool = self.tools[tool_name]
        missing = [p for p in tool["params"] if p not in kwargs]
        if missing:
            return f"缺少参数：{', '.join(missing)}"
        return tool["func"](**{p: kwargs[p] for p in tool["params"]})


def main():
    agent = HelloAgent()
    print("=" * 50)
    print("       Hello Agent — 入门示例")
    print("=" * 50)
    print(agent.list_tools())
    print()

    # 示例调用 / Example calls
    examples = [
        ("say_hello", {"name": "世界"}),
        ("get_weather", {"city": "北京"}),
        ("calculate", {"expression": "3 * (4 + 5)"}),
        ("get_weather", {"city": "深圳"}),
    ]

    for tool_name, params in examples:
        result = agent.run(tool_name, **params)
        param_str = ", ".join(f"{k}={v!r}" for k, v in params.items())
        print(f"[{tool_name}({param_str})]")
        print(f"  => {result}")
        print()


if __name__ == "__main__":
    main()
