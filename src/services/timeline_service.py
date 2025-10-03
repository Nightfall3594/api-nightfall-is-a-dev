from __future__ import annotations
from typing import List

from src.repos import *
from src.models.db import Article, Project, Thought


class TimelineService:

    def __init__(
        self,
        articles: ArticleRepository = InMemoryArticleRepository(),
        projects: ProjectRepository = InMemoryProjectRepository(),
        thoughts: ThoughtRepository = InMemoryThoughtRepository()
    ):
        self._article_repo = articles
        self._project_repo = projects
        self._thought_repo = thoughts

    def get_timelines(self) -> List[Article | Project | Thought]:

        return sorted(
            [
               *self._article_repo.get_all(with_body=False),
               *self._project_repo.get_all(),
               *self._thought_repo.get_all()
            ],
            key=lambda t: t.date_created
        )
