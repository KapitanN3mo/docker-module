from fastapi import FastAPI
from schemas.note import NoteCreate, NoteRead
from datetime import datetime
from uuid import uuid4
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

notes: list[NoteRead] = [
    NoteRead(
        title="Это тестовая заметка",
        content="Привет мир!",
        tags=["test", "default"],
        created_at=datetime.now(),
        updated_at=datetime.now(),
        id=str(uuid4()),
        author_id="system",
    )
]


@app.get("/notes")
def get_all_notes() -> list[NoteRead]:
    return notes


@app.post("/notes")
def create_note(note_data: NoteCreate):
    new_note = NoteRead(
        **note_data.model_dump(),
        created_at=datetime.now(),
        updated_at=datetime.now(),
        id=str(uuid4()),
        author_id="system",
    )
    notes.append(new_note)
    return new_note
