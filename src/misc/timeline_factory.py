from src.models.db import Article, Thought, Project
from src.models.dto import TimelineItem, TimelineArticleItem, TimelineProjectItem, TimelineThoughtItem
from pydantic import model_validator


class TimelineFactory:

    @staticmethod
    def create_timeline_item(item: TimelineItem):

        if isinstance(item, Article):
            return TimelineArticleItem.model_validate(item)


        elif isinstance(item, Thought):
            return TimelineThoughtItem.model_validate(item)


        elif isinstance(item, Project):
            return TimelineProjectItem.model_validate(item)

        else:
            raise TypeError("Unknown item type")
