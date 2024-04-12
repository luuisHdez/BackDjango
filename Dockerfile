# Imagen oficial de python
FROM python:3.12.2

# Directorio de trabajo
WORKDIR /app

# Instala las dependencias del proyecto
RUN apt-get update && \
    apt-get install -y netcat-openbsd && \
    rm -rf /var/lib/apt/lists/*

# Copia el archivo de requisitos primero, para aprovechar la caché de capas de Docker
# RUN pip install --no-cache-dir -r requirements.txt
COPY ./requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY ./ ./

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
    
