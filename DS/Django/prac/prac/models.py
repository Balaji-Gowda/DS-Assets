from django.db import models
from django.forms.fields import CharField
from django.forms.widgets import HiddenInput


class rvw(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=20)


class sample(models.Model):
    Id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=100)
    Place = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tbl_sample'
