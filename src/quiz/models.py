from datetime import datetime

from sqlalchemy import INTEGER, TIMESTAMP, String
from sqlalchemy.orm import Mapped, mapped_column

from src.base import Base


class Question(Base):
    __tablename__ = 'questions'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    question_id: Mapped[int] = mapped_column(INTEGER, nullable=False, unique=True)
    question: Mapped[str] = mapped_column(String(300), nullable=False, unique=True)
    answer: Mapped[str] = mapped_column(String(300), nullable=False)
    create_dt: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=False)

    def __repr__(self) -> str:
        return f'Question(id={self.id!r}, question_id={self.question_id!r}, create_dt={self.create_dt!r})'
