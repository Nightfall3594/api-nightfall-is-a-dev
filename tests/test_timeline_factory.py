from src.misc import TimelineFactory
from src.models.db import *
from src.models.dto import *


def test_model_validation():

    project = Project(id=0, title='TestArticle', date_created=datetime.now(), link="", description="")
    article = Article(id=1, title='TestProject', date_created=datetime.now(), article_slug="")
    thought = Thought(id=2, body='TestThoughtBody', date_created=datetime.now())

    assert isinstance(TimelineProjectItem.model_validate(project), TimelineProjectItem)
    assert isinstance(TimelineArticleItem.model_validate(article), TimelineArticleItem)
    assert isinstance(TimelineThoughtItem.model_validate(thought), TimelineThoughtItem)


def test_timeline_factory():

    project = Project(id=0, title='TestArticle', date_created=datetime.now(), link="", description="")
    article = Article(id=1, title='TestProject', date_created=datetime.now(), article_slug="")
    thought = Thought(id=2, body='TestThoughtBody', date_created=datetime.now())

    timeline = [project, article, thought]

    timeline = [TimelineFactory.create_timeline_item(item) for item in timeline]

    assert isinstance(timeline[0], TimelineProjectItem)
    assert isinstance(timeline[1], TimelineArticleItem)
    assert isinstance(timeline[2], TimelineThoughtItem)


