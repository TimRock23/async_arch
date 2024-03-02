FROM python:3.11-alpine

WORKDIR /usr/src/auth_app

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev && apk add libffi-dev
RUN pip install --upgrade pip

COPY app/requirements.txt ./
RUN pip install -r requirements.txt

COPY . .
