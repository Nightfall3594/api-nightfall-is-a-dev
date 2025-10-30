from datetime import datetime

from src.models.db import Project
from src.repos.project_repo import PostgresProjectRepository


def test_project_get_all(get_test_db):

    repo = PostgresProjectRepository(get_test_db)
    output = repo.get_all()

    assert len(output) == 3
    assert output[0].title == "Personal Portfolio"
    assert output[1].title == "Task Tracker"
    assert output[2].title == "API Playground"


def test_project_get_by_title(get_test_db):
    repo = PostgresProjectRepository(get_test_db)
    output = repo.get_by_title("Personal Portfolio")

    assert output.title == "Personal Portfolio"
    assert output is not None


def test_project_get_by_title_null(get_test_db):
    repo = PostgresProjectRepository(get_test_db)
    output = repo.get_by_title("Nonexistent Title")

    assert output is None


def test_project_add(get_test_db):
    repo = PostgresProjectRepository(get_test_db)

    new_project = Project(
        title="New Project 1",
        description="New description",
        link="https://example.com",
        date_created=datetime.now()
    )

    repo.add(new_project)
    output = repo.get_by_title("New Project 1")

    assert output.title == "New Project 1"
    assert output is not None