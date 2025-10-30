from fastapi import Depends

from src.db_config import SessionLocal
from src.repos import *
from src.services import *
from src.repos import *


def get_db():
    with SessionLocal() as session:
        yield session
        session.commit()

# callbacks for dependency injection
def get_article_service():
    return ArticleService(PostgresArticleRepository(session=Depends(get_db)))


def get_project_service():
    return ProjectService(PostgresProjectRepository(session=Depends(get_db)))


def get_thought_service():
    return ThoughtService(PostgresThoughtRepository(session=Depends(get_db)))


def get_timeline_service():
    return TimelineService(
        articles = PostgresArticleRepository(session=Depends(get_db)),
        projects = PostgresProjectRepository(session=Depends(get_db)),
        thoughts = PostgresThoughtRepository(session=Depends(get_db)),
    )
