from datetime import datetime

from src.models.db import Article
from src.repos.article_repo import PostgresArticleRepository


def test_article_get_by_slug(get_test_db):

    repo = PostgresArticleRepository(session=get_test_db)
    output = repo.get_by_slug('writing_articles_in_markdown')

    assert output.title == 'Writing Articles in Markdown'
    assert output.article_slug == 'writing_articles_in_markdown'
    assert output is not None


def test_article_get_by_slug_empty(get_test_db):

    repo = PostgresArticleRepository(session=get_test_db)
    output = repo.get_by_slug('nonexistent_article')

    assert output is None


def test_article_get_all(get_test_db):

    repo = PostgresArticleRepository(session=get_test_db)
    output = repo.get_all()

    assert len(output) == 2

    assert output[0].title == 'Introduction to SQLAlchemy'
    assert output[0].article_slug == 'introduction_to_sqlalchemy'

    assert output[1].title == 'Writing Articles in Markdown'
    assert output[1].article_slug == 'writing_articles_in_markdown'


def test_article_add(get_test_db):
    repo = PostgresArticleRepository(session=get_test_db)
    repo.add(
        Article(
            title='Hello World',
            article_slug='hello_world',
            date_created=datetime.now(),
            last_edited=datetime.now(),
            body='Hello World'
        )
    )

    assert repo.get_by_slug('hello_world').title == 'Hello World'




