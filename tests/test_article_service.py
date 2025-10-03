from src.repos import *
from src.services import article_service
from src.services.article_service import ArticleService


def test_article_service_get():
    service = ArticleService(article_repo=InMemoryArticleRepository())

    articles = service.get_articles()
    in_memory_articles = InMemoryArticleRepository().get_all()

    # assert several key attributes
    assert list(map(lambda a: a.title, articles)) == list(map(lambda a: a.title, in_memory_articles))
    assert list(map(lambda a: a.article_slug, articles)) == list(map(lambda a: a.article_slug, in_memory_articles))
    assert list(map(lambda a: a.date_created, articles)) == list(map(lambda a: a.date_created, in_memory_articles))
    assert list(map(lambda a: a.last_edited, articles)) == list(map(lambda a: a.last_edited, in_memory_articles))


def test_article_service_get_by_slug():
    articles = ArticleService(article_repo=InMemoryArticleRepository())

    assert articles.get_article_by_slug("nonexistent_slug") is None

def test_article_service_get_by_title():
    articles = ArticleService(article_repo=InMemoryArticleRepository())

    assert articles.get_article_by_slug("article_slug_1").title == "title_1"



