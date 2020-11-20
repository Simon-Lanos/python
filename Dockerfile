# Dockerfile for Flask app
FROM python:3.7-slim

RUN python -m pip install --upgrade pip

WORKDIR /usr/src/app
COPY ./Flask /usr/src/app

# requirements.txt list python dependencies
RUN python -m pip install -r requirements.txt

EXPOSE 5000

CMD [ "python", "app.py" ]
