"""Calculator skill for Mini-OpenClaw.

Perform mathematical calculations.
"""


async def execute(params: dict) -> str:
    """Execute a calculation."""
    operation = params.get("operation", "")
    a = float(params.get("a", 0))
    b = float(params.get("b", 0))

    import math

    try:
        if operation == "add":
            result = a + b
        elif operation == "subtract":
            result = a - b
        elif operation == "multiply":
            result = a * b
        elif operation == "divide":
            if b == 0:
                return "Error: Division by zero"
            result = a / b
        elif operation == "power":
            result = a**b
        elif operation == "sqrt":
            result = a**0.5
        elif operation == "mod":
            result = a % b
        elif operation == "floor_div":
            result = a // b
        elif operation == "log":
            result = math.log(a, b) if b > 0 and a > 0 else "Error: log requires positive numbers"
        elif operation == "sin":
            result = math.sin(math.radians(a))
        elif operation == "cos":
            result = math.cos(math.radians(a))
        elif operation == "tan":
            result = math.tan(math.radians(a))
        elif operation == "factorial":
            result = math.factorial(int(a))
        elif operation == "abs":
            result = abs(a)
        elif operation == "round":
            result = round(a, int(b) if b else 0)
        else:
            return f"Unknown operation: {operation}"

        return f"Result: {result}"
    except Exception as e:
        return f"Error: {str(e)}"
