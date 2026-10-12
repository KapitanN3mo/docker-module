import pydantic
from pydantic import Field
from datetime import datetime


class BaseNote(pydantic.BaseModel):
    title: str = Field(max_length=64)
    content: str = Field(max_length=40000)
    tags: list[str] = ["test-tag"]


class NoteRead(BaseNote):
    id: int
    author_id: int
    created_at: datetime
    updated_at: datetime


class NoteCreate(BaseNote):
    author_id: int = 1
