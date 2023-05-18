from http import HTTPStatus

from httpx import AsyncClient, Response
from sqlalchemy import Delete, Select, delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from servises.servises import (add_unique_questions_in_db,
                               get_last_save_question)
from src.quiz.models import Question
from src.quiz.schemas import QuestionRead


async def test_add_unique_questions_in_db(test_session: AsyncSession):
    await add_unique_questions_in_db(session=test_session, quantity_questions=10)
    query: Select = select(Question)
    result = await test_session.execute(query)
    assert len(result.all()) == 10


async def test_add_questions(ac: AsyncClient, test_session: AsyncSession):
    result: Question = await get_last_save_question(session=test_session)
    response: Response = await ac.post('/quiz/add-questions', json={'questions_num': 10})
    assert response.status_code == HTTPStatus.OK
    assert QuestionRead(**response.json()).dict() == QuestionRead(**result.__dict__).dict()


async def test_add_questions_none(ac: AsyncClient, test_session: AsyncSession):
    stmt: Delete = delete(Question)
    await test_session.execute(stmt)
    await test_session.commit()
    response: Response = await ac.post('/quiz/add-questions', json={'questions_num': 10})
    assert response.status_code == HTTPStatus.OK
    assert response.json() is None
