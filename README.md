# Django + S3

**Set up**

To run the containers:
```
docker-compose up -d --build
``` 

To create the migration file, re-build the images, and spin up the new containers:

```
docker-compose exec web python manage.py makemigrations
docker-compose down -v
docker-compose up -d --build
docker-compose exec web python manage.py migrate
```

**Configurables**

In the `docker-compose.yml` file change `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` to your own user in AWS. 

**ACLS**

We have set `AWS_DEFAULT_ACL = 'public-read'` in `settings.py` which means the the permissions in the `banyan-cert-bucket` S3 bucket has ACLs enabled and all public access.

To turn this off, we would have to set `AWS_DEFAULT_ACL = None` in `settings.py`, disable ACLs and block all public access -- however this means you can't publicly read uploaded content. 

**Buckets**

Static content is stored in `'banyan-static-bucket'` and PDFs/certs are stored in `'banyan-cert-bucket'`
