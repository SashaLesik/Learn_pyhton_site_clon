FROM python:3.11.7-slim

ENV FLASK_APP=web_app 
ENV FLASK_ENV=development


RUN python -m pip install --upgrade pip

COPY requirements.txt .

RUN python -m pip install -r requirements.txt

# COPY web_app/ /web_app/web_app

COPY . .

# CMD flask --app --debug run --host 0.0.0.0 --port 8000