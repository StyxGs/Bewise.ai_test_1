from datetime import datetime

from pydantic import BaseModel, Field


class Question(BaseModel):
    class Config:
        orm_mode = True


class QuantityQuestions(Question):
    questions_num: int = Field(ge=1, le=100, default=1)


class QuestionRead(Question):
    id: int
    question_id: int
    question: str
    answer: str
    create_dt: datetime
