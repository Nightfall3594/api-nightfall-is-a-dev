from datetime import datetime

from src.models.db import Thought
from src.repos.thought_repo import PostgresThoughtRepository


def test_thought_get(get_test_db):

    repo = PostgresThoughtRepository(get_test_db)
    output = repo.get_all()

    assert len(output) == 3
    assert output[0].body == 'Learning is exponential when curiosity is sustained.'


def test_thought_add(get_test_db):

    repo = PostgresThoughtRepository(get_test_db)
    repo.add(
        Thought(
            date_created=datetime.fromisoformat("2025-08-03T20:10:00+00:00"),
            body= "Test Body"
        )
    )

    thoughts = repo.get_all()

    assert thoughts[0].body == 'Test Body'