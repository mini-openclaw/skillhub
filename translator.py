"""Translator skill for Mini-OpenClaw.

Translate text between languages.
"""


async def execute(params: dict) -> str:
    """Translate text."""
    text = params.get("text", "")
    target = params.get("to", "en")
    source = params.get("from", "auto")

    if not text:
        return "Error: Please provide 'text' to translate"

    try:
        import httpx

        async with httpx.AsyncClient(timeout=15.0) as client:
            url = "https://api.mymemory.translated.net/get"
            response = await client.get(url, params={"q": text, "langpair": f"{source}|{target}"})
            if response.status_code == 200:
                data = response.json()
                if data.get("responseStatus") == 200:
                    translated = data.get("responseData", {}).get("translatedText", "")
                    return f"Translation ({source} -> {target}): {translated}"
            return "Error: Translation failed"
    except Exception as e:
        return f"Error: {str(e)}"
