FROM python:2.7-slim

COPY . ./app
WORKDIR /app

RUN pip install -r requirements.txt

ENV FLASK_APP app.py
CMD flask run --host=0.0.0.0 -p $PORT
