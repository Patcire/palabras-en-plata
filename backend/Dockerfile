# backend/Dockerfile
FROM python:3.8.2

WORKDIR /app

COPY . /app

RUN pip install django && python -m django --version && pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]