# Pull base image
FROM python:3.9

#Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#Set work dir
RUN mkdir /code
WORKDIR /code

#Install dependencies
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system

#Copy project
COPY . /code/