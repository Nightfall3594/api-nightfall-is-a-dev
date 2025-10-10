from __future__ import annotations
from datetime import datetime
from typing import Literal, List

from pydantic import BaseModel, ConfigDict


class ArticleResponse(BaseModel):
    id: int
    title: str
    date_created: datetime
    last_edited: datetime
    article_slug: str
    body: str | None = None
    model_config = ConfigDict(from_attributes=True)

class ArticleListResponse(BaseModel):
    articles: List[ArticleResponse]

class ThoughtResponse(BaseModel):
    id: int
    body: str
    date_created: datetime = datetime.now()
    model_config = ConfigDict(from_attributes=True)

class ThoughtListResponse(BaseModel):
    thoughts: List[ThoughtResponse]
    model_config = ConfigDict(from_attributes=True)

class ProjectResponse(BaseModel):
    id: int
    title: str
    description: str
    link: str
    model_config = ConfigDict(from_attributes=True)

class ProjectListResponse(BaseModel):
    projects: List[ProjectResponse]



class TimelineItem(BaseModel):
    date_created: datetime
    model_config = ConfigDict(from_attributes=True)


class TimelineArticleItem(TimelineItem):
    id: int
    type: Literal["article_item"]
    title: str
    link: str
    date_created: datetime


class TimelineProjectItem(TimelineItem):
    id: int
    type: Literal["project_item"]
    title: str
    link: str
    date_created: datetime


class TimelineThoughtItem(TimelineItem):
    body: str
    model_config = ConfigDict(from_attributes=True)
    date_created: datetime


class TimelineResponse(BaseModel):
    items: List[TimelineArticleItem | TimelineProjectItem | TimelineThoughtItem]