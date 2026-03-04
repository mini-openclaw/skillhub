"""Code formatter skill for Mini-OpenClaw.

Format code using Prettier or similar.
"""


async def execute(params: dict) -> str:
    """Format code."""
    code = params.get("code", "")
    language = params.get("language", "javascript")

    if not code:
        return "Error: Please provide 'code' to format"

    try:
        import httpx

        async with httpx.AsyncClient(timeout=15.0) as client:
            response = await client.post(
                "https://api.prettier.io/format", params={"parser": language}, content=code
            )
            if response.status_code == 200:
                return f"Formatted ({language}):\n{response.text}"
            return "Error: Could not format code"
    except Exception as e:
        return f"Error: {str(e)}"
