from prac.models import sample
from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponseRedirect
from django import forms
from .forms import reviewform
from .models import rvw

from django.views.generic import ListView


class reviewList(ListView):  # listview
    model = rvw

# def home(request):
#     lis = sample.objects.filter(Place='US')
#     return render(request, 'home.html', {'lis': lis})


def review(request):

    if request.method == 'POST':
        form = reviewform(request.POST)
        if form.is_valid():
            # frm = rvw(name=form.cleaned_data['name'],
            #           password=form.cleaned_data['password'])
            # frm.save()
            form.save()  # only for modelforms
            return HttpResponseRedirect('ty1')
    else:
        form = reviewform()
    return render(request, "review.html", {"form": form})


def ty(request):
    return render(request, "tu.html")
