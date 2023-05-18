from fastapi import FastAPI

from src.quiz.router import router as router_quiz

app = FastAPI(
    description='Api для викторины',
    title='Викторина',
)

app.include_router(router_quiz)
