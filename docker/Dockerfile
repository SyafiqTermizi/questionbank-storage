FROM python:3.9-buster

ENV PYTHONUNBUFFERED 1
WORKDIR /app

RUN apt-get update && apt-get install pandoc -y

# Requirements are installed here to ensure they will be cached.
COPY pyproject.toml ./
RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry install
