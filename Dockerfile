FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=arq_vagas.settings
ENV LC_ALL=pt_BR.UTF-8

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev libpq-dev musl-dev

WORKDIR /app
COPY ../ /app

RUN pip install -r requirements.txt \
    && python manage.py collectstatic --no-input \
    && python manage.py migrate

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]