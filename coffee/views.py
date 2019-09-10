from django.shortcuts import render
from .models import coffee
# Create your views here.


def index(request):

    coffees = coffee.objects.all()

    return render(request, "index.html", {'coffees': coffees})