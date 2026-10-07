import pydantic
from pydantic import Field
from uuid import uuid4
from datetime import datetime


class BaseNote(pydantic.BaseModel):
    title: str = Field(max_length=64)
    content: str = Field(max_length=40000)
    tags: list[str]


class NoteRead(BaseNote):
    id: str
    author_id: str
    created_at: datetime
    updated_at: datetime


class NoteCreate(BaseNote):
    pass
    # id: str = Field(default_factory=lambda: str(uuid4()))
    # author_id: str = Field(default="unknown")
