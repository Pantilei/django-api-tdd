FROM python:3.10.4-alpine3.15
LABEL Author=Pantilei

ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /requirements.txt
# Install dependancies for psycopg2 python package
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmpl-build-deps \
    gcc libc-dev linux-headers postgresql-dev
# Install python packages
RUN pip install -r ./requirements.txt
# Remove temporary created dependancies
RUN apk del .tmpl-build-deps

RUN mkdir /app
# Set working directory for any subsequent instruction in docker file
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user
