from __future__ import annotations
from typing import List

from src.models.db import Thought
from src.repos import ThoughtRepository


class ThoughtService:

    def __init__(self, repository: ThoughtRepository):
        self._repository = repository


    def get_all(self) -> List[Thought]:
        return self._repository.get_all()


    def add(self, thought: Thought) -> None:
        self._repository.add(thought)
