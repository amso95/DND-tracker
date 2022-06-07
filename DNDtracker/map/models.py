from django.db import models
from city.models import City
from django.conf import settings


class Map(models.Model):
    name = models.CharField(max_length=255, blank = False)
    pdf = models.FileField(upload_to=settings.MEDIA_ROOT , max_length=255, blank = False)
    city = models.ForeignKey(City, default=1, on_delete=models.CASCADE)
