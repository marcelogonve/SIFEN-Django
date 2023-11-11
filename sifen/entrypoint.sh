#!/bin/sh

# Se espera a que la base de datos esté lista
# TODO: Se agregará el script más adelante

# Se aplican las migraciones
python manage.py migrate

# Luego se ejecuta el comando principal (se inicia el servidor de Django)
exec "$@"