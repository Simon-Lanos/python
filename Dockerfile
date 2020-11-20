# Dockerfile for Flask app
FROM python:3.6-slim

RUN python -m pip install --upgrade pip

WORKDIR /usr/src/app
COPY ./Flask .

RUN python -m pip install -r /usr/src/app/requirements.txt

EXPOSE 5000

CMD python app.py
