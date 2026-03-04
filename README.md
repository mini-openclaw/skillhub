# Mini-OpenClaw SkillHub

This directory contains the structure for hosting a community SkillHub for Mini-OpenClaw.

## Quick Start

### 1. Hosting Your Own SkillHub

Create a GitHub repository with this structure:

```
your-repo/
├── skills.json          # Skill manifest
├── weather.py          # Skill implementations
├── calculator.py
└── ...
```

The `skills.json` must contain:

```json
{
  "version": "1.0.0",
  "name": "Your SkillHub",
  "description": "Description of your skill collection",
  "skills": [
    {
      "name": "skill_name",
      "version": "1.0.0",
      "description": "What this skill does",
      "author": "Your Name",
      "tags": ["tag1", "tag2"],
      "category": "utility",
      "homepage": "https://...",
      "repository": "https://github.com/your-repo/your-repo"
    }
  ]
}
```

### 2. Creating a Skill

Create a Python file with an `execute` function:

```python
# myskill.py

async def execute(params: dict) -> str:
    """Execute the skill with given parameters."""
    action = params.get("action", "default")
    
    if action == "greet":
        name = params.get("name", "World")
        return f"Hello, {name}!"
    
    return "Unknown action"

# Or use the full skill class for more control:

from dataclasses import dataclass

@dataclass
class SkillMetadata:
    name: str
    version: str
    description: str
    author: str = ""
    tags: list = None

class MySkill:
    metadata = SkillMetadata(
        name="myskill",
        version="1.0.0",
        description="My custom skill",
        author="You"
    )
    
    async def initialize(self):
        """Called when skill loads."""
        pass
    
    async def execute(self, params: dict) -> str:
        """Execute the skill."""
        return "Result"
    
    async def shutdown(self):
        """Called when skill unloads."""
        pass

def get_skill():
    return MySkill()
```

### 3. Installing from a Custom Hub

```python
from mini_openclaw.skills import get_skill_manager

manager = get_skill_manager()

# Set custom hub URL
manager.hub.hub_url = "https://your-username.github.io/your-repo"

# Search for skills
results = await manager.search("weather")

# Install a skill
await manager.install_from_hub("weather")
```

## Using Skills

### Local Skills

Place skill files in `./skills/` directory:

```
mini-openclaw/
├── skills/
│   ├── weather.py
│   └── calculator.py
└── ...
```

### Running Skills

```python
from mini_openclaw.skills import get_skill_manager

async def main():
    manager = get_skill_manager()
    
    # Initialize all local skills
    await manager.initialize()
    
    # List installed skills
    for skill in manager.list_installed():
        print(f"- {skill.name} v{skill.version}")
    
    # Get tools from skills
    tools = manager.get_tools()
    
    # Use a skill directly
    skill = manager.registry.get("weather")
    if skill:
        result = await skill.execute({"location": "London", "action": "current"})
        print(result)
```

## Skill API

### Skill Metadata

```python
@dataclass
class SkillMetadata:
    name: str           # Unique identifier
    version: str        # Semantic version
    description: str    # Human-readable description
    author: str = ""    # Skill author
    tags: list[str] = [] # Searchable tags
    category: str = "general" # Skill category
    homepage: str = ""  # Documentation URL
    repository: str = "" # Source code URL
```

### Skill Interface

```python
class Skill:
    metadata: SkillMetadata
    enabled: bool = True
    
    async def initialize(self) -> None:
        """Called when skill loads. Setup resources here."""
        pass
    
    async def execute(self, params: dict) -> str:
        """Execute the skill with parameters.
        
        Args:
            params: Dictionary of parameters
            
        Returns:
            str: Result of execution
        """
        pass
    
    async def shutdown(self) -> None:
        """Called when skill unloads. Cleanup here."""
        pass
    
    def to_tool(self):
        """Convert skill to LangChain tool."""
        pass
```

## Environment Variables

- `SKILL_HUB_URL` - Default skill hub URL
- `SKILLS_DIR` - Local skills directory (default: `./skills`)
