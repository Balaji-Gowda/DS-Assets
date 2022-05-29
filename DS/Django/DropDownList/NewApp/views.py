from django.shortcuts import render
from NewApp import models
from NewApp.models import catalogs


def display(request):
    print(request.GET["inp"])
    cat = catalogs.objects.values_list('cluster', flat=True).distinct()
    bus = catalogs.objects.values_list('business', flat=True).distinct()
    ct = catalogs.objects.values_list('category', flat=True).distinct()
    cod = catalogs.objects.values_list('code', flat=True).distinct()

    return render(request, 'res.html', {'cat': cat, 'bus': bus, 'ct': ct, 'cod': cod})
    #val = request.GET['cluster']
    # val2 = request.GET['business']
    # val3 = request.GET['category']
    # val4 = request.GET['code']
    # dat = catalogs.objects.filter(
    #     business=val2, category=val3, code=val4)

    # return render(request, 'disp.html', {'cat': cat, 'bus': bus, 'ct': ct, 'cod': cod, 'dat': dat})
