import datetime
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    current = datetime.datetime.now()
    return render(request, "newyear/year.html", {
        "newyear" : current.month == 1 and current.day == 1
    })
    