from fastapi import Depends

from src.db_config import SessionLocal
from src.repos import *
from src.services import *
from src.repos import *


# TODO: Replace Depends() with generator expression

def get_db():
    with SessionLocal() as session:
        yield session
        session.commit()

# callbacks for dependency injection
def get_article_service():
    return ArticleService(PostgresArticleRepository(next(get_db())))


def get_project_service():
    return ProjectService(PostgresProjectRepository(next(get_db())))


def get_thought_service():
    return ThoughtService(PostgresThoughtRepository(next(get_db())))


def get_timeline_service():
    return TimelineService(
        articles = PostgresArticleRepository(next(get_db())),
        projects = PostgresProjectRepository(next(get_db())),
        thoughts = PostgresThoughtRepository(next(get_db())),
    )
