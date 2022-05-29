from django.db import models

# Create your models here.


class heads(models.Model):
    head = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    off = models.BooleanField(default=False)
