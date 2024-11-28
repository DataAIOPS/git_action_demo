FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt app.py /app

RUN apt-get update && apt-get install -y bash

RUN pip install -r requirements.txt

CMD ["python", "app.py"]

