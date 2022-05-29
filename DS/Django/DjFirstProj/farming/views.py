from farming.models import heads
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
   
    headLis = heads.objects.all()
    return render(request, 'index.html', {'heading': 'Balaji_Heading', 'headLis': headLis})
    return render(request, 'home.html', {'heading': 'Balaji_Heading', 'headLis': headLis})
