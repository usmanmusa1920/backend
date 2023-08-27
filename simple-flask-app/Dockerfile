FROM python:3.8.5-alpine

LABEL name="simple-flask-app"
LABEL version="0.0.1"
LABEL description="A simple flask application using docker"
MAINTAINER Usman Musa

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . /app

WORKDIR /app

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]
