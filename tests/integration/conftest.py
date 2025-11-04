import pytest
import sqlalchemy
import sqlalchemy.orm as orm
from src.models.db import *

@pytest.fixture(scope="package", autouse=True)
def get_test_db():

    from datetime import datetime

    test_engine = sqlalchemy.create_engine('postgresql+psycopg2://postgres:secret_password@localhost:5613/testdb')
    Base.metadata.drop_all(test_engine)
    Base.metadata.create_all(test_engine)
    test_SessionLocal = orm.sessionmaker(bind=test_engine)


    # seed data
    articles = [
        Article(
            article_slug="introduction_to_sqlalchemy",
            title="Introduction to SQLAlchemy",
            date_created=datetime.fromisoformat("2025-01-10T10:00:00+00:00"),
            last_edited=datetime.fromisoformat("2025-01-10T10:00:00+00:00"),
            body=(
                "# Introduction to SQLAlchemy\n"
                "SQLAlchemy is a Python ORM that lets you interact with databases using Python classes instead of raw SQL.\n\n"
                "## Example\n"
                "```python\nfrom sqlalchemy import create_engine\nengine = create_engine(\"sqlite:///example.db\")\n```"
            ),
        ),
        Article(
            article_slug="writing_articles_in_markdown",
            title="Writing Articles in Markdown",
            date_created=datetime.fromisoformat("2025-02-14T15:30:00+00:00"),
            last_edited=datetime.fromisoformat("2025-02-15T09:00:00+00:00"),
            body=(
                "# Writing in Markdown\n"
                "Markdown allows you to format text easily using symbols.\n\n"
                "- **Bold text** with `**bold**`\n"
                "- *Italic text* with `*italic*`\n"
                "- Code blocks with triple backticks."
            ),
        ),
    ]

    thoughts = [
        Thought(
            body="Simplicity in code often leads to better maintainability.",
            date_created=datetime.fromisoformat("2025-03-01T12:00:00+00:00"),
        ),
        Thought(
            body="Sometimes, doing nothing is also a decision.",
            date_created=datetime.fromisoformat("2025-03-02T08:45:00+00:00"),
        ),
        Thought(
            body="Learning is exponential when curiosity is sustained.",
            date_created=datetime.fromisoformat("2025-03-03T20:10:00+00:00"),
        ),
    ]

    projects = [
        Project(
            title="Personal Portfolio",
            description="A simple portfolio website showcasing my projects and articles.",
            link="https://example.com/portfolio",
            date_created=datetime.fromisoformat("2025-01-05T14:00:00+00:00"),
        ),
        Project(
            title="Task Tracker",
            description="A minimalistic web app to manage tasks using Flask and SQLite.",
            link="https://github.com/user/task-tracker",
            date_created=datetime.fromisoformat("2025-02-01T09:30:00+00:00"),
        ),
        Project(
            title="API Playground",
            description="A RESTful API built with FastAPI demonstrating CRUD operations.",
            link="https://github.com/user/api-playground",
            date_created=datetime.fromisoformat("2025-02-20T11:15:00+00:00"),
        ),
    ]

    # seed data
    with test_SessionLocal() as session:
        [session.add(i) for i in articles]
        [session.add(i) for i in thoughts]
        [session.add(i) for i in projects]
        session.commit()

        yield session

