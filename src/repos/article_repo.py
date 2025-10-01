from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import datetime
from typing import List

from src.models.db import Article

class ArticleRepository(ABC):
    @abstractmethod
    def get_by_slug(self, slug) -> Article:
        pass

    @abstractmethod
    def get_all(self, with_body = False) -> List[Article]:
        pass

    @abstractmethod
    def add(self, article) -> None:
        pass


class InMemoryArticleRepository(ArticleRepository):
    def __init__(self):
        self.articles: List[Article] = [
            Article(
                id=1,
                article_slug='article_slug_1',
                title='title_1',
                date_created=datetime(2022, 5, 14, 8, 30),
                last_edited=datetime(2023, 8, 19, 11, 15),
                body='Hello, World1!'
            ),
            Article(
                id=2,
                article_slug='article_slug_2',
                title='title_2',
                date_created=datetime(2021, 7, 22, 14, 45),
                last_edited=datetime(2024, 3, 10, 9, 30),
                body='Hello, World2!'
            ),
        ]

    def get_by_slug(self, slug: str) -> Article | None:
        return next((article for article in self.articles if article.article_slug == slug), None)

    def get_all(self, with_body = False) -> List[Article]:

        if with_body:
            return self.articles

        else:
            articles = self.articles

            # Remove body manually for testing only
            # In a real repo you would simply not query it in the db
            for i in articles:
                i.body = ""

            return articles

    def add(self, article: Article):
        self.articles.append(article)

