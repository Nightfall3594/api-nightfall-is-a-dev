FROM python:3.13-bookworm

# install poetry
RUN apt-get update
RUN apt-get install pipx -y
RUN pipx install poetry


# install dependencies
COPY pyproject.toml .
COPY poetry.* .
RUN pipx run poetry install --without dev

COPY . .

EXPOSE 80

CMD ["pipx", "run", "poetry", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]




