from django import forms
from django.db import models
from django.db.models.base import Model
from django.forms import fields
from .models import sample, rvw


# class reviewform(forms.Form):
#     md = sample.objects.all()
#     uname = forms.CharField(max_length=20)
#     pwd = forms.CharField(max_length=20)

class reviewform(forms.ModelForm):
    class Meta:

        model = rvw
        fields = '__all__'
        # fields = ['un', 'psd']
        # exclude = ['extra']
        # labels={
        #     'md name':'intrst name'
        #     'model field':'instrat label'
        # }

        # error_messages = {
        #     "un":{
        #         "required":"field is mandatory"
        #         "max_length":"content should be limited"
        #     }
        # }
