FROM python:3.8-slim-buster

RUN apt-get update \
	&& pip install poetry

WORKDIR /app

COPY ./poetry.lock ./pyproject.toml /app/

RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi

COPY . /app