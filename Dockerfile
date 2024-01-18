FROM python:3.11.7-slim

ENV FLASK_APP=web_app 
ENV FLASK_ENV=development

WORKDIR /web_app/

RUN python -m pip install --upgrade pip

COPY requirements.txt .

RUN python -m pip install -r requirements.txt


COPY . .

# CMD flask run --host 0.0.0.0 --port 8000