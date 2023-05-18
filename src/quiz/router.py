from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from servises.servises import (add_unique_questions_in_db,
                               get_last_save_question)
from src.database_contion import get_async_session
from src.quiz.models import Question
from src.quiz.schemas import QuantityQuestions

router: APIRouter = APIRouter(
    prefix='/quiz',
    tags=['quiz']
)


@router.post('/add-questions')
async def add_questions(questions_num: QuantityQuestions, session: AsyncSession = Depends(get_async_session)):
    try:
        last_question: Question = await get_last_save_question(session=session)
        await add_unique_questions_in_db(session=session, quantity_questions=questions_num.dict()['questions_num'])
        return last_question
    except Exception:
        raise HTTPException(status_code=400, detail='Ошибка на стороне сервера.')
