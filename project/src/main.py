from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.notes import router as notes_router
from routers.user import router as user_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(notes_router, prefix="/notes")
app.include_router(user_router, prefix="/auth")