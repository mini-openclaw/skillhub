"""GIF search skill for Mini-OpenClaw.

Search and get GIFs from GIPHY.
"""


async def execute(params: dict) -> str:
    """Search for GIFs."""
    query = params.get("query", "")

    if not query:
        return "Error: Please provide a 'query' to search"

    try:
        import httpx

        api_key = "dc6zaTOxFJmzC"  # Public beta key
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(
                "https://api.giphy.com/v1/gifs/search",
                params={"api_key": api_key, "q": query, "limit": 1},
            )
            if response.status_code == 200:
                data = response.json()
                gifs = data.get("data", [])
                if gifs:
                    gif = gifs[0]
                    return f"GIF: {gif.get('title', query)}\n{gif.get('images', {}).get('original', {}).get('url', '')}"
            return "No GIFs found"
    except Exception as e:
        return f"Error: {str(e)}"
