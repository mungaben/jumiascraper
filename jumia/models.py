from django.db import models


class Jumia(models.Model):
    filename = models.CharField(max_length=100)
    filedownload = models.FileField()

    created_at = models.DateTimeField(auto_now_add=True)


# Create your models here.
