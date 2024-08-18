FROM python:3.12

#ARG PIP_INDEX_URL

#ENV PIP_INDEX_URL=$PIP_INDEX_URL
WORKDIR /app
COPY ./src /app

RUN pip install -U pip && pip install  -r requirements.txt

EXPOSE 8001
COPY ./src /workdir
WORKDIR /app

