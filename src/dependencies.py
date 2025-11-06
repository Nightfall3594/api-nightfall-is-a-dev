from fastapi import Depends

from src.db_config import SessionLocal
from src.services import *
from src.repos import *


def get_db():
    with SessionLocal() as session:
        yield session
        session.commit()

# callbacks for dependency injection
def get_article_service(db = Depends(get_db)):
    return ArticleService(PostgresArticleRepository(db))


def get_project_service(db = Depends(get_db)):
    return ProjectService(PostgresProjectRepository(db))


def get_thought_service(db = Depends(get_db)):
    return ThoughtService(PostgresThoughtRepository(db))


def get_timeline_service(db = Depends(get_db)):
    return TimelineService(
        articles = PostgresArticleRepository(db),
        projects = PostgresProjectRepository(db),
        thoughts = PostgresThoughtRepository(db),
    )
