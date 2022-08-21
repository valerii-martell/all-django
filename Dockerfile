# pull official base image
FROM python:3.9.6-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
RUN mkdir /app
WORKDIR /app
# copy project
ADD . /app

# install dependencies
RUN pip install --upgrade pip
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
# COPY ./requirements.txt .
RUN pip install -r requirements.txt --no-deps --no-dependencies
EXPOSE 8000
CMD python manage.py wait_for_db && python manage.py migrate && python manage.py runserver 0.0.0.0:8000

