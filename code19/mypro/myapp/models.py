from django.db import models


# Create your models here.


class photo_model(models.Model):
    photo = models.ImageField(upload_to='Images')

