from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from database import get_db
from schemas.note import NoteRead, NoteCreate
from repos.notes import NoteRepo
from typing import Sequence

router = APIRouter()


@router.get("/")
async def get_all_notes(db: AsyncSession = Depends(get_db)) -> Sequence[NoteRead]:
    return await NoteRepo(db).get_all()


@router.post("/")
async def create_note(note: NoteCreate, db: AsyncSession = Depends(get_db)) -> NoteRead:
    return await NoteRepo(db).create(note)
