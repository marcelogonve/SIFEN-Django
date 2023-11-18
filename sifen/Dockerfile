# Imagen oficial de Python como imagen base
FROM python:3.10

# Actualiza los paquetes e instala el cliente de PostgreSQL
RUN apt-get update && apt-get install -y postgresql-client

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Se copia el archivo requirements.txt al directorio de trabajo
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Se copian los archivos restantes del proyecto
COPY . .

# Copiar el script de entrada y dar permisos de ejecución
COPY entrypoint.sh /app/
RUN chmod +x /app/entrypoint.sh

# Se expone el puerto 8000
EXPOSE 8000

# Configurar el script de entrada como punto de entrada
ENTRYPOINT ["/app/entrypoint.sh"]

# Comando por defecto para iniciar el servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
