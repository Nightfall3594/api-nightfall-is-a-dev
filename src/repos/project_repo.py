from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import datetime
from typing import List

from src.models.db import Project


class ProjectRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Project]:
        pass

    @abstractmethod
    def add(self, project: Project) -> None:
        pass

    @abstractmethod
    def get_by_title(self, title: str) -> Project:
        pass


class InMemoryProjectRepository(ProjectRepository):

    def __init__(self):
        self.projects = [
            Project(
                id=1,
                title="My First Project1",
                description="My First Project1 yayy",
                link="https://myfirstproject1.com",
                date_created=datetime(2020, 1, 10, 10, 30),
            ),
            Project(
                id=2,
                title="My First Project2",
                description="My First Project2 yayy",
                link="https://myfirstproject2.com",
                date_created=datetime(2021, 4, 22, 17, 0),
            ),
            Project(
                id=3,
                title="My First Project3",
                description="My First Project3 yayy",
                link="https://myfirstproject3.com",
                date_created=datetime(2023, 7, 15, 14, 45),
            ),
        ]


    def get_all(self) -> List[Project]:
        return self.projects


    def add(self, project: Project) -> None:
        self.projects.append(project)


    def get_by_title(self, title: str) -> Project | None:
        return next((p for p in self.projects if p.title == title), None)