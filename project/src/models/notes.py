from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy import BigInteger, String, DateTime, func, ForeignKey
from datetime import datetime
from .base import Base


class Note(Base):
    __tablename__ = "notes"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    title: Mapped[str] = mapped_column(String(64))
    content: Mapped[str] = mapped_column(String(40000))
    author_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.id"))
    author = relationship("User", back_populates="notes")
    # tag
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
