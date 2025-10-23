from __future__ import annotations
from datetime import datetime
from typing import Literal, List

from pydantic import BaseModel, ConfigDict

class BaseResponse(BaseModel):
    date_created: datetime


# Single-item responses
class ArticleResponse(BaseResponse):
    id: int
    title: str
    last_edited: datetime
    article_slug: str
    body: str | None = None
    model_config = ConfigDict(from_attributes=True)


class ThoughtResponse(BaseResponse):
    id: int
    body: str
    model_config = ConfigDict(from_attributes=True)


class ProjectResponse(BaseResponse):
    id: int
    title: str
    description: str
    link: str
    model_config = ConfigDict(from_attributes=True)


# List Responses
class ThoughtListResponse(BaseModel):
    thoughts: List[ThoughtResponse]
    model_config = ConfigDict(from_attributes=True)


class ArticleListResponse(BaseModel):
    articles: List[ArticleResponse]


class ProjectListResponse(BaseModel):
    projects: List[ProjectResponse]


# Timeline Responses
class TimelineItem(BaseModel):
    date_created: datetime
    model_config = ConfigDict(from_attributes=True)


class TimelineArticleItem(TimelineItem):
    id: int
    type: Literal["article_item"] = "article_item"
    title: str
    article_slug: str


class TimelineProjectItem(TimelineItem):
    id: int
    type: Literal["project_item"] = "project_item"
    title: str
    link: str


class TimelineThoughtItem(TimelineItem):
    id: int
    type: Literal["thought_item"] = "thought_item"
    body: str


class TimelineResponse(BaseModel):
    items: List[TimelineArticleItem | TimelineProjectItem | TimelineThoughtItem]