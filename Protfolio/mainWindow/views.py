from django.shortcuts import render
from django.http import HttpResponse

from .models import New
from .models import Info
from .models import Biography

biography = {
        "name": "Евгений",
        "surname": "Круглик",
        "age": 20
}

def home(request):
    data = {
        "title": "Главная страница",
        "info": Info.objects.all(),
    }
    return render(request, "home.html", data)
    #return HttpResponse('<h2>Привет мир!</h2>')

def sheet_biography(request):
    data = {
        "title": "Биография",
        "biography": Biography.objects.all(),
    }
    return render(request, "biography.html", data)

def portfolio_list (request):
    data = {
        "title": "Портфолио",
        "biography": Biography.objects.all(),
    }
    return render(request, "portfolio_list.html", data)
