from pathlib import Path
import yaml
from pydantic import BaseModel

BASE_DIR = Path(__file__).resolve().parent.parent / "prompts"


class PromptConfig(BaseModel):
    version: str
    system_prompt: str
    few_shot: list = []


def load_prompts(version: str) -> PromptConfig:
    main_file = BASE_DIR / f"{version}.yaml"
    if not main_file.exists():
        raise FileNotFoundError(f"Menu file not found: {main_file}")
    with open(main_file, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    config = PromptConfig(**data)
    return config
