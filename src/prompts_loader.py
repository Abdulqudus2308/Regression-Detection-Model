from pathlib import Path
import yaml
from typing import Literal
from pydantic import BaseModel

BASE_DIR = Path(__file__).resolve.parent().parent()


class PromptConfig(BaseModel):
    version: str = "v1"
    system_prompt: str
    few_shot: Literal["category", "summary"]


def load_prompts(version):
    main_file = BASE_DIR / "Prmopts" / "v1.yaml"
    if not main_file.exists():
        raise FileNotFoundError(f"Menu file not found: {main_file}")
    with open(main_file, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    config = PromptConfig(**data)
