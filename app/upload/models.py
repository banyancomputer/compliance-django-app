from django.db import models
from hello_django.storage_backends import S3CertBucket
from django.conf import settings

# Create your models here.


class CertUploadModel(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    if settings.USE_S3:
        file = models.FileField(storage=S3CertBucket())
    else:
        file = models.FileField(upload_to='')


class KnowYourMiner(models.Model):
    minerAddress = models.CharField(max_length=80)
    geography = models.CharField(max_length=80)
    reputation = models.CharField(max_length=80)
    dataCenterTier = models.IntegerField()


class HITRUST(models.Model):
    miner = models.CharField(max_length=80)
    auditor = models.CharField(max_length=80)
    expiration = models.CharField(max_length=80)
    link = models.CharField(max_length=80)
