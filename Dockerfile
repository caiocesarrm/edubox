FROM python:3.6.11-slim-buster

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

COPY ./requirements/ /app/requirements/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /app/requirements/production.txt

COPY . /app/

#ENTRYPOINT ["gunicorn"]
#CMD ["--bind","0.0.0.0:50010","wsgi:app","-w","4", "--reload", "--worker-class=gthread", "--threads=40"]
