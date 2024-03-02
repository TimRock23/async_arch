FROM python:3.11-alpine

WORKDIR /app

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev && apk add libffi-dev
RUN pip install --upgrade pip

COPY app/requirements.txt ./
RUN pip install -r requirements.txt
COPY --chown=user app/ /app/

RUN python manage.py collectstatic --noinput

EXPOSE 80

CMD gunicorn --chdir /app auth.wsgi:application -b :8000 --reload
