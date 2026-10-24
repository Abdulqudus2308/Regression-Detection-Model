from typing import Literal
from pydantic import BaseModel, ConfigDict, Field


class EmailResult(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    email_category: Literal["billing", "technical", "account", "general"]
    summary: str = Field(min_length=1, max_length=300)
