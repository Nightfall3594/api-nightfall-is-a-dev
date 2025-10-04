from datetime import datetime

from src.models.db import Thought
from src.repos import InMemoryThoughtRepository
from src.services.thought_service import ThoughtService


def test_thought_service_get():
    repo = InMemoryThoughtRepository()
    service = ThoughtService(repo)

    assert service.get_all() == repo.get_all()


def test_thought_service_add():
    repo = InMemoryThoughtRepository()
    service = ThoughtService(repo)

    new_thought = Thought(
        id=4,
        body="Hello world!",
        date_created=datetime(2020, 12, 31, 23, 59, 59)
    )
    service.add(new_thought)

    assert service.get_all()[-1] == new_thought