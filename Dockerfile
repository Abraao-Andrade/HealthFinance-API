# syntax=docker/dockerfile:1.0.0
FROM python:3.11.0-slim-buster

WORKDIR /app
ENV FLASK_APP run.py

COPY requirements.txt requeriments.txt
RUN pip install --upgrade pip
RUN pip install -r requeriments.txt

COPY . .

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
