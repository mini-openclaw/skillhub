"""Image generation skill for Mini-OpenClaw.

Generate images from text using free APIs.
"""


async def execute(params: dict) -> str:
    """Generate an image."""
    prompt = params.get("prompt", "")

    if not prompt:
        return "Error: Please provide a 'prompt' for image generation"

    try:
        import httpx

        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.get(
                "https://image.pollinations.ai/prompt/" + prompt.replace(" ", "%20"),
                params={"width": 512, "height": 512, "nologo": "true"},
            )
            if response.status_code == 200:
                import base64

                img_b64 = base64.b64encode(response.content).decode()
                return f"Generated image for '{prompt}':\ndata:image/png;base64,{img_b64}"
            return "Error: Could not generate image"
    except Exception as e:
        return f"Error: {str(e)}"
