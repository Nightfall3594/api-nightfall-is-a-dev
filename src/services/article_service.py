from __future__ import annotations

from src.models.db import Article
from src.repos.article_repo import ArticleRepository, InMemoryArticleRepository


class ArticleService:
    def __init__(self, article_repo: ArticleRepository = InMemoryArticleRepository()):
        self._article_repo: ArticleRepository = article_repo

    def get_articles(self) -> list[Article]:
        return self._article_repo.get_all(with_body=False)

    def get_article_by_slug(self, slug: str) -> Article:
        return self._article_repo.get_by_slug(slug)

    def add_article(self, article: Article) -> None:
        if self._article_repo.get_by_slug(article.article_slug) is None:
            self._article_repo.add(article)

        else:
            raise RuntimeError('Article already exists')