from langchain_core.tools import tool

@tool
def addition(a: float, b: float) -> dict:
    """Add two numbers and return steps"""
    return {
        "result": a + b,
        "steps": [
            f"Step 1: Take first number = {a}",
            f"Step 2: Take second number = {b}",
            f"Step 3: Add them → {a} + {b} = {a + b}"
        ]
    }


@tool
def subtraction(a: float, b: float) -> dict:
    """Subtract second number from first with steps"""
    return {
        "result": a - b,
        "steps": [
            f"Step 1: Take first number = {a}",
            f"Step 2: Take second number = {b}",
            f"Step 3: Subtract → {a} - {b} = {a - b}"
        ]
    }


@tool
def multiplication(a: float, b: float) -> dict:
    """Multiply two numbers with steps"""
    return {
        "result": a * b,
        "steps": [
            f"Step 1: Take first number = {a}",
            f"Step 2: Take second number = {b}",
            f"Step 3: Multiply → {a} × {b} = {a * b}"
        ]
    }

@tool
def division(a:float, b:float) -> dict : 
    """Divides two numbers with steps"""
    return {
        "result": a / b,
        "steps": [
            f"Step 1: Take first number = {a}",
            f"Step 2: Take second number = {b}",
            f"Step 3: Multiply → {a} / {b} = {a / b}"
        ]
    }

MATH_TOOLS = [addition, subtraction, multiplication, division]