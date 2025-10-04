from src.models.db import Project
from src.repos import ProjectRepository, InMemoryProjectRepository


class ProjectService:
    def __init__(self, repository: ProjectRepository = InMemoryProjectRepository()):
        self._repository = repository

    def get_all(self):
        return self._repository.get_all()

    def add(self, project: Project) -> None:
        if not self._repository.get_by_title(project.title):
            self._repository.add(project)

        else:
            raise RuntimeError("Project already exists")