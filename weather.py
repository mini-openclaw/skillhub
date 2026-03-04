"""Weather skill for Mini-OpenClaw.

A sample skill that fetches weather information.
"""

import asyncio
from typing import Any

try:
    from ..skills import Skill, SkillMetadata
except ImportError:
    from mini_openclaw.skills import Skill, SkillMetadata


async def get_weather(params: dict) -> str:
    """Get weather information for a location."""
    import httpx

    location = params.get("location", "")
    if not location:
        return "Error: Location is required"

    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(f"https://wttr.in/{location}?format=%c%t+%h+%w")
            if response.status_code == 200:
                return f"Weather for {location}: {response.text}"
            return f"Could not fetch weather for {location}"
    except Exception as e:
        return f"Error fetching weather: {str(e)}"


async def get_forecast(params: dict) -> str:
    """Get weather forecast for a location."""
    import httpx

    location = params.get("location", "")
    days = params.get("days", 3)

    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(f"https://wttr.in/{location}?format=%d+%c+%t")
            if response.status_code == 200:
                lines = response.text.strip().split("\n")
                forecast = "Forecast:\n"
                for line in lines[:days]:
                    forecast += f"  {line}\n"
                return forecast
            return f"Could not fetch forecast for {location}"
    except Exception as e:
        return f"Error fetching forecast: {str(e)}"


class WeatherSkill(Skill):
    """Skill for getting weather information."""

    def __init__(self):
        metadata = SkillMetadata(
            name="weather",
            version="1.0.0",
            description="Get current weather and forecast for any location",
            author="Mini-OpenClaw",
            tags=["weather", "forecast", "utility"],
            category="information",
        )
        super().__init__(metadata=metadata)

    async def initialize(self) -> None:
        """Initialize the weather skill."""
        pass

    async def execute(self, params: dict) -> str:
        """Execute the weather skill."""
        action = params.get("action", "current")

        if action == "current":
            return await get_weather(params)
        elif action == "forecast":
            return await get_forecast(params)
        else:
            return f"Unknown action: {action}. Use 'current' or 'forecast'."

    async def shutdown(self) -> None:
        """Shutdown the weather skill."""
        pass


def get_skill() -> "WeatherSkill":
    """Get the weather skill instance."""
    return WeatherSkill()
