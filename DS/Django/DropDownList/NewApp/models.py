from django.db import models
from django.db.models.fields import CharField


class catalogs(models.Model):
    cluster = models.CharField(max_length=100)
    business = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    code = models.IntegerField()

    class Meta:
        db_table = 'catalogs'
