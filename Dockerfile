FROM python:3.9.12-slim-buster
ENV PYTHONUNBUFFERED=1
WORKDIR /django
COPY ./requirements.txt requirements.txt
RUN pip install --upgrade pip \
    pip install -r requirements.txt