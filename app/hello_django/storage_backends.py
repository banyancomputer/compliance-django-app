from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

# Storage class for writing certs to S3
class S3CertBucket(S3Boto3Storage):
    if settings.USE_S3:
        bucket_name = settings.AWS_CERT_BUCKET_NAME
        location = settings.AWS_CERT_BUCKET_LOCATION
        custom_domain = settings.AWS_CERT_BUCKET_CUSTOM_DOMAIN
