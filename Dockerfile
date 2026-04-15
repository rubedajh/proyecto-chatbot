FROM python:3.11-slim

RUN apt-get update && apt-get install -y python3-tk && apt-get clean

WORKDIR /app

COPY . .

ENV DB_PATH=/app/base_datos.json

CMD ["python", "app.py"]