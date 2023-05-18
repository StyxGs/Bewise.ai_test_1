from datetime import datetime

import httpx
from httpx import Response
from sqlalchemy import Result, Select, select
from sqlalchemy.dialects.postgresql import Insert, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.quiz.models import Question


async def add_unique_questions_in_db(session: AsyncSession, quantity_questions: int) -> None:
    async with httpx.AsyncClient() as client:
        data_finally: list = []
        while quantity_questions:
            response: Response = await client.get(f'https://jservice.io/api/random?count={quantity_questions}')
            data_a: dict = response.json()
            query: Select = select(Question.question_id).filter(
                Question.question_id.in_([question['id'] for question in data_a])
            )
            result_select: Result = await session.scalars(query)
            recurring_questions: list = result_select.all()
            quantity_questions: int = len(recurring_questions)
            check: list = list(filter(lambda question: question['id'] not in recurring_questions, data_a))
            data_finally.extend(check)
        data: list[dict] = [
            {'question_id': question['id'], 'question': question['question'],
             'answer': question['answer'],
             'create_dt': datetime.strptime(question['created_at'], '%Y-%m-%dT%H:%M:%S.%fZ'), }
            for question in data_finally
        ]
        stmt: Insert = insert(Question).values(data).on_conflict_do_nothing(index_elements=['question_id'])
        await session.execute(stmt)
        await session.commit()


async def get_last_save_question(session: AsyncSession):
    query: Select = select(Question).order_by(Question.id.desc()).limit(1)
    result: Result = await session.scalars(query)
    return result.first()
