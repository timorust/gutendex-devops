FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y libpq-dev gcc curl \
    && apt-get clean

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .
COPY wait-for-it.sh .
COPY entrypoint.sh .
RUN chmod +x wait-for-it.sh entrypoint.sh
RUN mkdir -p /app/catalog_files/tmp/cache/epub

ENTRYPOINT ["./entrypoint.sh"]


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
