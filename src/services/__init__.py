from src.services.article_service import ArticleService
from src.services.project_service import ProjectService
from src.services.thought_service import ThoughtService
from src.services.timeline_service import TimelineService

from src.repos import *



# callbacks for dependency injection
def get_article_service():
    return ArticleService(InMemoryArticleRepository())


def get_project_service():
    return ProjectService(InMemoryProjectRepository())


def get_thought_service():
    return ThoughtService(InMemoryThoughtRepository())


def get_timeline_service():
    return TimelineService(
        articles = InMemoryArticleRepository(),
        projects = InMemoryProjectRepository(),
        thoughts = InMemoryThoughtRepository(),
    )


__all__ = [
    'ArticleService',
    'ProjectService',
    'ThoughtService',
    'TimelineService',

    'get_article_service',
    'get_project_service',
    'get_thought_service',
    'get_timeline_service',
]