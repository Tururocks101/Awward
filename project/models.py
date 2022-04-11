from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class projects(models.Model):

    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1500)
    image_url = models.CharField(max_length=520)

    def __str__(self):
        return self.name
