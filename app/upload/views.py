from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

from .models import CertUploadModel


def image_upload(request):
    if request.method == 'POST':
        image_file = request.FILES['image_file']
        image_type = request.POST['image_type']
        upload = CertUploadModel(file=image_file)
        upload.save()
        image_url = upload.file.url
        return render(request, 'upload.html', {
            'image_url': image_url
        })
    return render(request, 'upload.html')
