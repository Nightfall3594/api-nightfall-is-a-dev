from datetime import datetime

from src.models.db import Project
from src.repos import InMemoryProjectRepository
from src.services.project_service import ProjectService

import pytest


def test_project_service_get():

    repo = InMemoryProjectRepository()
    service = ProjectService(repo)

    assert service.get_all() == repo.get_all()
    assert len(service.get_all()) == len(repo.get_all())


def test_project_service_add():

    service = ProjectService()

    new_project = Project(id=4, title="New Project", description="New description", link="https://example.com", date_created=datetime.now())
    service.add(new_project)

    assert service.get_all()[-1] == new_project


def test_project_service_add_duplicate():

    service = ProjectService()
    duplicate = service.get_all()[0]

    with pytest.raises(RuntimeError, match="Project already exists"):
        service.add(duplicate)