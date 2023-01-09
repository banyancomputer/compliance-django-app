from django.db import models
from hello_django.storage_backends import StaticStorage, PDFBucket

# Create your models here.


class StaticStorageModel(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(storage=StaticStorage())


class PDFBucketModel(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(storage=PDFBucket())
