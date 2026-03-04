"""URL shortener skill for Mini-OpenClaw.

Shorten long URLs.
"""


async def execute(params: dict) -> str:
    """Shorten a URL."""
    url = params.get("url", "")

    if not url:
        return "Error: Please provide 'url' to shorten"

    try:
        import httpx

        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.post("https://ulvis.net/api.php", data={"url": url})
            if response.status_code == 200:
                return f"Shortened URL: {response.text.strip()}"
            return "Error: Could not shorten URL"
    except Exception as e:
        return f"Error: {str(e)}"
