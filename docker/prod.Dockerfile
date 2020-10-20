FROM python:3.9-buster

ENV PYTHONUNBUFFERED 1
WORKDIR /app

# install pandoc
RUN apt-get update && apt-get install pandoc -y

# Requirements are installed here to ensure they will be cached.
COPY . /app
RUN pip install --upgrade pip && pip install poetry
RUN poetry install
