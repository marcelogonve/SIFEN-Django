# Imagen oficial de python como imagen base
FROM python:3.10

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Se copia el archivo requirements.txt al directorio de trabajo
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Se copia el contenido del directorio actual al directorio de trabajo
COPY  . .

# Se expone el puerto 8000
EXPOSE 8000

# Se ejecuta el comando para iniciar el servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]