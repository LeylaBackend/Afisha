FROM python:3.8

ENV PYTHONWRITEBYCODE 1

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY . .