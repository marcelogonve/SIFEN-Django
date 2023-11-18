#!/bin/sh

# Se espera a que la base de datos esté lista
until PGPASSWORD=$DATABASE_PASSWORD psql -h "$DATABASE_HOST" -U "$DATABASE_USER" -d "$DATABASE_NAME" -c '\q'; do
  >&2 echo "Postgres no está listo - esperando..."
  sleep 1
done

>&2 echo "Postgres está listo - continuando..."

# Se aplican las migraciones
python manage.py migrate

# Luego se ejecuta el comando principal (se inicia el servidor de Django)
exec "$@"