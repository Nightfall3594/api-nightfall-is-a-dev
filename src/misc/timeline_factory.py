from src.models.dto import TimelineItem, TimelineArticleItem, TimelineProjectItem, TimelineThoughtItem
from pydantic import model_validator


class TimelineFactory:

    @staticmethod
    def create_timeline_item(item: TimelineItem):

        if item.type == "Article":
            return TimelineArticleItem.model_validate(item)


        if item.type == "Thought":
            return TimelineThoughtItem.model_validate(item)


        if item.type == "Project":
            return TimelineProjectItem.model_validate(item)

        else:
            raise TypeError("Unknown item type")
