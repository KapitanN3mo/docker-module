from sqlalchemy.ext.asyncio import AsyncSession
from typing import Sequence
from schemas.note import NoteCreate
from sqlalchemy import select
from models import Note


class NoteRepo:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self) -> Sequence[Note]:
        res = await self.db.execute(select(Note))  # = SELECT * FROM "notes"
        return res.scalars().all()

    async def create(self, note_data: NoteCreate) -> Note:
        new_note = Note(
            title=note_data.title,
            content=note_data.content,
            author_id=note_data.author_id,
        )
        self.db.add(new_note)
        await self.db.commit()
        await self.db.refresh(new_note)
        return new_note
