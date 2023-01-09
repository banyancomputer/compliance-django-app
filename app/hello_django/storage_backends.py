from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    bucket_name = 'banyan-static-bucket'
    location = 'static'
    # default_acl = 'public-read'


# class PublicMediaStorage(S3Boto3Storage):
#     location = 'media'
#     default_acl = 'public-read'
#     file_overwrite = False


class PDFBucket(S3Boto3Storage):
    bucket_name = 'banyan-cert-bucket'
    location = 'media'
    default_acl = 'public-read'
    custom_domain = '{}.s3.amazonaws.com'.format(bucket_name)
