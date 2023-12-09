from django.shortcuts import render
from django.http import HttpResponse

from .models import New

biography = {
        "name": "Евгений",
        "surname": "Круглик",
        "age": 20
}

def home(request):
    data = {
        "news": New.objects.all(),
        "title": "Главная страница"
    }
    return render(request, "home.html", data)
    return HttpResponse('<h2>Привет мир!</h2>')

def sheet_biography(request):
    data = {
        "biography": biography,
        "title": "Биография"
    }
    return render(request, "biography.html", data)
