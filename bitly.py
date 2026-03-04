"""Bitly shortener skill for Mini-OpenClaw.

Shorten URLs using Bitly.
"""


async def execute(params: dict) -> str:
    """Shorten a URL using Bitly."""
    url = params.get("url", "")
    token = params.get("token", "")  # Optional: use your own token

    if not url:
        return "Error: Please provide 'url' to shorten"

    try:
        import httpx

        headers = {"Authorization": f"Bearer {token}"} if token else {}
        async with httpx.AsyncClient(timeout=10.0, headers=headers) as client:
            response = await client.post(
                "https://api-ssl.bitly.com/v4/shorten", json={"long_url": url}
            )
            if response.status_code in (200, 201):
                data = response.json()
                return f"Shortened URL: {data.get('link', 'Error')}"
            return (
                "Error: Could not shorten URL. Note: Requires Bitly API token for custom shortener."
            )
    except Exception as e:
        return f"Error: {str(e)}"
