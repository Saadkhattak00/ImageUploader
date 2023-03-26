from django.db import models


# Create your models here.
class ImageModel(models.Model):
    photo = models.ImageField(upload_to='MyImages'),
    date = models.DateTimeField(auto_now_add=True),
