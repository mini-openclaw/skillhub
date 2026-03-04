"""QRCode generator skill for Mini-OpenClaw.

Generate QR codes for text or URLs.
"""


async def execute(params: dict) -> str:
    """Generate a QR code."""
    data = params.get("data", "")
    size = int(params.get("size", 200))

    if not data:
        return "Error: Please provide 'data' to encode"

    try:
        import httpx

        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(
                f"https://api.qrserver.com/v1/create-qr-code/",
                params={"size": f"{size}x{size}", "data": data},
            )
            if response.status_code == 200:
                import base64

                img_b64 = base64.b64encode(response.content).decode()
                return f"QR Code for '{data}':\ndata:image/png;base64,{img_b64}"
            return "Error: Could not generate QR code"
    except Exception as e:
        return f"Error: {str(e)}"
