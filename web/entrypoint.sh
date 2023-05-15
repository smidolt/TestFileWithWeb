#!/bin/sh
set -e  # If a command fails, stop the script immediately

# Wait for the database to become available
until PGPASSWORD=$POSTGRES_PASSWORD psql -h db -U $POSTGRES_USER -c '\q'; do
  echo "Postgres is unavailable - sleeping"  # Print a message to the console
  sleep 1  # Pause execution for 1 second
done

# Execute init.sql
PGPASSWORD=$POSTGRES_PASSWORD psql -h db -U $POSTGRES_USER -f /init.sql

# Start the server
exec python server.py
