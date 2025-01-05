FROM python:3.13.1-alpine3.21

WORKDIR /app

RUN pip install --no-cache-dir flask

COPY templates /app/templates

COPY MainScores.py scores.txt /app/

EXPOSE 5000

CMD ["python", "MainScores.py"]




