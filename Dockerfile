FROM python:3.11.4-alpine3.18

ENV RUNNER_TOKEN ""
ENV ORG_NAME ""

WORKDIR /app

ADD delete-runners.py /app/delete-runners.py
