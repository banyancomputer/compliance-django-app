# Compliance Django App
This repository contains the Django app for managing and serving our Compliance data.
It implements a simple Django app that:
- is meant to run in a docker container
- allows users to upload files either to:
  - a local directory
  - or a remote S3 bucket. The container must have the proper credentials to write to the bucket.

## Requirements
Assuming you want to run and test in only in docker, all you need are:
- `docker`
- `docker-compose`

## Development Setup

### Setup
Copy `/env/.env.dev-sample` to `/env/.env.dev` and update the values as needed:
```
# Django App Configuration
DEBUG=1 # Whether to run in debug mode or not. Set to 1 for development.
SECRET_KEY=foo # A secret key that django uses.
DJANGO_ALLOWED_HOSTS=* # A list of hosts that django will allow
SQL_ENGINE=django.db.backends.postgresql # The database engine to use. Do not change.

# Django Admin Configuration
DJANGO_SUPERUSER_USERNAME=admin # The username of the superuser
DJANGO_SUPERUSER_PASSWORD=admin # The password of the superuser
DJANGO_SUPERUSER_EMAIL=your@email.com # The email of the superuser

# Database Connection Configuration
SQL_DATABASE=hello_django_dev # The name of the database to use
SQL_USER=hello_django # The username of the database user
SQL_PASSWORD=hello_django # The password of the database user
SQL_HOST=db # The name of the database container. Do not change.
SQL_PORT=5432 # The default port for postgres

# S3 Backend Configuration. Simply set USE_S3 to FALSE for development.
USE_S3=FALSE # Whether or not to use S3 for storing uploaded files.
```
Copy `/env/.env.db-sample` to `/env/.env.db` and update the values to reflect the connection to your database:
```
# Database connection configuration
POSTGRES_DB=hello_django_dev
POSTGRES_USER=hello_django
POSTGRES_PASSWORD=hello_django
```

### Running

Run the following commands to build and run the docker container:
```
docker-compose up -d --build
```
This should start a database container and a django app container.
Before the server is run, the container handles:
- creating migrations
- running migrations
- creating a superuser
- collecting static files

The container then executes the `runserver` command.
The django app should be running at `localhost:8000`.

Run the following command to stop the containers:
```
docker-compose down
```

### Testing

TODO!


## Production Setup

### Setup

Copy `/env/.env.prod-sample` to `/env/.env.prod` and update the values as needed:
```
# Django App Configuration
DEBUG=0 # Whether to run in debug mode or not. Set to 1 for emulated production.
SECRET_KEY=CHANGE_ME # A secret key that django uses
DJANGO_ALLOWED_HOSTS=CHANGE_ME # A list of hosts that django will allow
SQL_ENGINE=django.db.backends.postgresql # The database engine to use

# Django Admin Configuration
DJANGO_SUPERUSER_USERNAME=admin # The username of the superuser
DJANGO_SUPERUSER_PASSWORD=CHANGE_ME # The password of the superuser
DJANGO_SUPERUSER_EMAIL=CHANGE@ME.com # The email of the superuser

# Database Connection Configuration
SQL_DATABASE=hello_django_dev # The name of the database to use
SQL_USER=hello_django # The username of the database user
SQL_PASSWORD=hello_django # The password of the database user
SQL_HOST=db # The name of the database container. Do not change.
SQL_PORT=5432 # The default port for postgres

# S3 Backend Configuration
USE_S3=TRUE # Whether or not to use S3 for storing uploaded files
AWS_ACCESS_KEY_ID=ABCDEFGHIJKL # The AWS access key id to use for S3. Must have write access to the bucket.
AWS_SECRET_ACCESS_KEY=VERYVERYSECRET # The AWS secret access key to use for S3. Must have write access to the bucket.
AWS_CERT_BUCKET_NAME=cert-bucket # The name of the bucket to use for storing certificates
AWS_REGION=us-east-2 # The AWS region to use for S3
```

Copy `/env/.env.db-sample` to `/env/.env.db` and update the values to reflect the connection to your database:
```
# Database connection configuration
POSTGRES_DB=hello_django_dev
POSTGRES_USER=hello_django
POSTGRES_PASSWORD=hello_django
```

### Running

Run the following commands to build and run the docker container:
```
docker-compose -f docker-compose.prod.yml up -d --build
```
This should start a database container, and nginx container, and a django app container.
The nginx container is configured to serve static files and proxy requests to the django app container.
The django app is run behind gunicorn.
Before the django app is run, the container handles:
- creating migrations
- running migrations
- creating a superuser
- collecting static files

The container then executes the `gunicorn` command.
The nginx server should be running at `localhost:1337`.

Run the following command to stop the containers:
```
docker-compose -f docker-compose.prod.yml down
```

### Testing

TODO!


