#!/bin/bash

# Wait for DB
echo "Waiting for PostgreSQL..."
while ! nc -z db 5432; do
  sleep 1
done
echo "PostgreSQL started."

# Run migrations and start server
python manage.py migrate
python manage.py collectstatic --noinput

exec "$@"