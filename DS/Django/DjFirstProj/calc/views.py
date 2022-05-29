from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse


from farming.models import heads
# Create your views here.


def home(request):
    headLis = heads.objects.all()
    return render(request, 'home.html', {'name': 'ChanduBalaji ...', 'headLis': headLis})


def add(request):
    num3 = int(request.POST['num1'])
    num4 = int(request.POST['num2'])
    res = num3+num4
    return render(request, "result.html", {"result": res})
