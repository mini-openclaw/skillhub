"""Random fact skill for Mini-OpenClaw.

Get interesting random facts.
"""


async def execute(params: dict) -> str:
    """Get a random fact."""
    try:
        import httpx

        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get("https://uselessfacts.jsph.pl/api/v2/facts/random")
            if response.status_code == 200:
                data = response.json()
                return f"Random Fact: {data.get('text', 'No fact found')}"
            return "Error: Could not fetch fact"
    except Exception as e:
        return f"Error: {str(e)}"
