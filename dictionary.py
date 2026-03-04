"""Dictionary skill for Mini-OpenClaw.

Get definitions and meanings of words.
"""


async def execute(params: dict) -> str:
    """Get word definition."""
    word = params.get("word", "").strip()

    if not word:
        return "Error: Please provide a 'word' to look up"

    try:
        import httpx

        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
            if response.status_code == 200:
                data = response.json()
                if isinstance(data, list) and data:
                    entry = data[0]
                    meanings = []
                    for meaning in entry.get("meanings", [])[:2]:
                        part = meaning.get("partOfSpeech", "")
                        defs = meaning.get("definitions", [])
                        if defs:
                            definition = defs[0].get("definition", "")
                            meanings.append(f"  ({part}) {definition}")
                    result = f"Word: {entry.get('word', word)}\n" + "\n".join(meanings)
                    return result
            return f"Definition not found for '{word}'"
    except Exception as e:
        return f"Error: {str(e)}"
