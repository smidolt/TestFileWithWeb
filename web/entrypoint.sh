#!/bin/sh
set -e

# Ждем, пока база данных станет доступной
until PGPASSWORD=$POSTGRES_PASSWORD psql -h db -U $POSTGRES_USER -c '\q'; do
  echo "Postgres is unavailable - sleeping"
  sleep 1
done

# Выполняем init.sql
PGPASSWORD=$POSTGRES_PASSWORD psql -h db -U $POSTGRES_USER -f /init.sql

# Запускаем сервер
exec python server.py
