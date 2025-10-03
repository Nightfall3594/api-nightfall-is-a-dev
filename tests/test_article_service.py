import pytest

from src.repos import *
from src.services.article_service import ArticleService


def test_article_service_get():
    repo = InMemoryArticleRepository()
    service = ArticleService(repo)

    assert service.get_articles() == repo.get_all()
    assert len(service.get_articles()) == len(repo.get_all())


def test_article_service_get_by_fake_slug():
    articles = ArticleService(InMemoryArticleRepository())

    assert articles.get_article_by_slug("nonexistent_slug") is None


def test_article_service_get_by_slug():
    repo = InMemoryArticleRepository()
    articles = ArticleService(repo)

    article_1 = articles.get_articles()[0]

    assert articles.get_article_by_slug(article_1.article_slug) == repo.get_all()[0]


def test_article_service_add_duplicate():
    service = ArticleService(InMemoryArticleRepository())
    duplicate_article = service.get_article_by_slug("article_slug_1")

    with pytest.raises(RuntimeError, match='Article already exists'):
        service.add_article(duplicate_article)
