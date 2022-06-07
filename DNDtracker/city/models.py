from django.db import models
from django.conf import settings

class City(models.Model):
    name = models.CharField(max_length=255, blank = False)
    pdf = models.FileField(upload_to=settings.MEDIA_ROOT , max_length=255, blank = False)
