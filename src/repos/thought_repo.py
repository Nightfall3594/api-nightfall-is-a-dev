from abc import ABC, abstractmethod
from datetime import datetime
from typing import List

from src.models.db import Thought


class ThoughtRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[Thought]:
        pass

    @abstractmethod
    def add(self, thought: Thought):
        pass


class InMemoryThoughtRepository(ThoughtRepository):

    def __init__(self):
        self.thoughts: List[Thought] = [
            Thought(
                id=1,
                body="This is a thought1",
                date_created=datetime(2021, 5, 14, 8, 30),
            ),
            Thought(
                id=2,
                body="This is a thought2",
                date_created=datetime(2022, 11, 3, 15, 45)
            ),
            Thought(
                id=3,
                body="This is a thought3",
                date_created=datetime(2023, 7, 19, 12, 0)
            ),
        ]

    def get_all(self) -> List[Thought]:
        return self.thoughts

    def add(self, thought: Thought):
        self.thoughts.append(thought)
