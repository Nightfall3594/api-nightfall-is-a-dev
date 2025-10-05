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


class TimelineArticleItem(TimelineItem):
    id: int
    type: Literal["article_item"]
    title: str
    link: str

class TimelineProjectItem(TimelineItem):
    id: int
    type: Literal["project_item"]
    title: str
    link: str

class TimelineThoughtItem(TimelineItem):
    body: str
    type: Literal["thought_item"]


class TimelineResponse(TimelineItem):
    items: List[TimelineArticleItem | TimelineProjectItem | TimelineThoughtItem]