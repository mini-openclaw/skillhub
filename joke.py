"""Joke skill for Mini-OpenClaw.

Get random jokes.
"""


async def execute(params: dict) -> str:
    """Get a joke."""
    category = params.get("category", "")

    try:
        import httpx

        async with httpx.AsyncClient(timeout=10.0) as client:
            url = "https://v2.jokeapi.dev/joke/Any"
            if category:
                url = f"https://v2.jokeapi.dev/joke/{category.title()}"
            response = await client.get(url)
            if response.status_code == 200:
                data = response.json()
                if data.get("type") == "single":
                    return data.get("joke", "No joke found")
                else:
                    return f"{data.get('setup', '')}\n{data.get('delivery', '')}"
            return "Error: Could not fetch joke"
    except Exception as e:
        return f"Error: {str(e)}"
