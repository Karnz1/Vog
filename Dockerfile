FROM python:3.13.1-alpine3.21

RUN pip install --no-cache-dir flask

WORKDIR /app

COPY templates /app/templates

COPY MainScores.py /app

EXPOSE 5000

CMD ["python", "MainScores.py"]
