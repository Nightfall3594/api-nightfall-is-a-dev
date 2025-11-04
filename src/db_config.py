import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

_DATABASE_USER = os.environ.get('DATABASE_USER')
_DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD')
_DATABASE_HOST = os.environ.get('DATABASE_HOST')
_DATABASE_PORT = os.environ.get('DATABASE_PORT')
_DATABASE_NAME = os.environ.get('DATABASE_NAME')

_DATABASE_URL = f"postgresql+psycopg2://{_DATABASE_USER}:{_DATABASE_PASSWORD}@{_DATABASE_HOST}:{_DATABASE_PORT}/{_DATABASE_NAME}"

_engine = create_engine(_DATABASE_URL)


SessionLocal = sessionmaker(bind=_engine)
