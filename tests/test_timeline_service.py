from datetime import datetime

from src.services.timeline_service import TimelineService


def test_timeline_get():

    timeline_service: TimelineService = TimelineService()
    timeline = timeline_service.get_timelines()

    assert timeline == sorted(timeline, key=lambda t: t.date_created)