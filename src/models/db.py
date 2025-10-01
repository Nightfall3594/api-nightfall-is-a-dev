from datetime import datetime

from sqlalchemy import *
from sqlalchemy.orm import declarative_base, Mapped, mapped_column


Base = declarative_base()

class Article(Base):
    __tablename__ = 'article'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    article_slug: Mapped[str] = mapped_column(String(255))
    title: Mapped[str] = mapped_column(String(255))
    date_created: Mapped[datetime] = mapped_column(DateTime)
    last_edited: Mapped[datetime] = mapped_column(DateTime)
    body: Mapped[str] = mapped_column(Text)


class Thought(Base):
    __tablename__ = 'thought'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    body: Mapped[str] = mapped_column(Text)
    date_created: Mapped[datetime] = mapped_column(DateTime)


class Project(Base):
    __tablename__ = 'project'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(Text)
    link: Mapped[str] = mapped_column(Text)
    date_created: Mapped[datetime] = mapped_column(DateTime)
