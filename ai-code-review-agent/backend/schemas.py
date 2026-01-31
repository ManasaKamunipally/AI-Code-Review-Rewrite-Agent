from pydantic import BaseModel


class CodeRequest(BaseModel):
    code: str
    language: str
    focus_areas: list[str]
