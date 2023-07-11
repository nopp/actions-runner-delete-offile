FROM python:3.11.4-alpine3.18

ENV GHUB_PAT ""
ENV ORG_NAME ""

WORKDIR /app

ADD delete-runners.py /app/delete-runners.py
ADD requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# CMD ["python", "delete-runners.py"]
