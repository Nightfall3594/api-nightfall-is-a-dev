from typing import List
from http.client import HTTPException

from fastapi import FastAPI, Depends

from src.misc import TimelineFactory
from src.models.dto import *
from src.services import *

app = FastAPI()


@app.get('/ping')
def ping():
    return {'ping': 'pong'}  # note: for testing connectivity only


@app.get('/timeline', response_model=TimelineResponse)
async def timeline(
    timeline_service: TimelineService = Depends(TimelineService)
) -> TimelineResponse:

    timelines = timeline_service.get_timelines()
    timelines = [TimelineFactory.create_timeline_item(item) for item in timelines]
    return TimelineResponse(items=timelines)


@app.get('/articles/{article_slug}', response_model=ArticleResponse)
async def article(
    article_slug: str,
    service: ArticleService = Depends(get_article_service)
):
    article_obj: ArticleResponse = service.get_article_by_slug(article_slug)
    if not article_obj:
        raise HTTPException(404, 'Article not found')
    else:
        return ArticleResponse.model_validate(article_obj)


@app.get('/articles', response_model=ArticleListResponse)
async def articles(
    service: ArticleService = Depends(get_article_service)
) -> ArticleListResponse:
    article_list = [ArticleResponse.model_validate(s) for s in service.get_articles()]
    return ArticleListResponse(articles=article_list)


@app.get('/thoughts', response_model=ThoughtListResponse)
async def thoughts(
    service: ThoughtService = Depends(get_thought_service)
) -> ThoughtListResponse:
    thoughts_list = [ThoughtResponse.model_validate(t) for t in service.get_all()]
    return ThoughtListResponse(thoughts=thoughts_list)


@app.get('/projects', response_model=ProjectListResponse)
async def projects(
    service: ProjectService = Depends(get_project_service)
) -> ProjectListResponse:

    projects = [ProjectResponse.model_validate(p) for p in service.get_all()]
    return ProjectListResponse(projects=projects)