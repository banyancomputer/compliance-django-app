#!/bin/sh

echo "Starting the application..."

# Wait for the database to be ready
while ! nc -z $SQL_HOST $SQL_PORT; do
  sleep 0.1
done

echo "PostgreSQL started"

# Run migrations and collect static files

echo "Running Flush.."
python manage.py flush --no-input
echo "Running Make Migrations.."
python manage.py makemigrations upload
echo "Running Migrate.."
python manage.py migrate
echo "Running Collect Static.."
python manage.py collectstatic --no-input --clear
echo "Creating Super User.."
python manage.py createsuperuser --no-input

echo "DB Migrations and Collect Static Files Complete"

# Start server
exec "$@"