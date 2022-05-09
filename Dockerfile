FROM python:3.10.4-alpine3.15
LABEL Author=Pantilei

ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /requirements.txt

RUN pip install -r ./requirements.txt

RUN mkdir /app
# Set working directory for any subsequent instruction in docker file
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user
