FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./docker/django_start /django_start
RUN sed -i 's/\r//' /django_start
RUN chmod +x /django_start
