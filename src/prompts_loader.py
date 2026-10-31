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
    if data is None:
        raise ValueError(f"Prompt file is empty: {main_file}")
    config = PromptConfig(**data)
    if version != config.version:
        raise ValueError(
            f"Asked for {version} but the file says {config.version}: {main_file}"
        )
    return config
