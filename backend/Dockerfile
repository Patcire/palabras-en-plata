FROM python:3.8.2

WORKDIR /app

COPY . /app

# Instalar las dependencias del proyecto (incluyendo Django)
RUN pip install --no-cache-dir -r requirements.txt

# Crear y aplicar las migraciones
RUN python manage.py makemigrations api
RUN python manage.py migrate

# Comando para ejecutar el servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
