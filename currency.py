"""Currency converter skill for Mini-OpenClaw.

Convert between currencies using exchange rates.
"""


async def execute(params: dict) -> str:
    """Convert currency."""
    from_currency = params.get("from", "").upper()
    to_currency = params.get("to", "").upper()
    amount = float(params.get("amount", 0))

    if not from_currency or not to_currency:
        return "Error: Please provide 'from', 'to', and 'amount'"

    try:
        import httpx

        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(
                f"https://api.exchangerate.host/latest?base={from_currency}&symbols={to_currency}"
            )
            if response.status_code == 200:
                data = response.json()
                rate = data.get("rates", {}).get(to_currency, 0)
                if rate:
                    result = amount * rate
                    return f"{amount} {from_currency} = {result:.2f} {to_currency} (Rate: {rate})"
            return "Error: Could not fetch exchange rate"
    except Exception as e:
        return f"Error: {str(e)}"
