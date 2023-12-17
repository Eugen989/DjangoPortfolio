from django.shortcuts import render
from django.http import HttpResponse

from .models import New
from .models import Info
from .models import Biography
from .models import Portfolio


biography = {
        "name": "Евгений",
        "surname": "Круглик",
        "age": 20
}

def home(request):
    src_text = []
    for i in range(len(Portfolio.objects.all())):
        src_text.append(f"mainWindow/media/img_{i}/im_1.png")
    data = {
        "title": "Главная страница",
        "info": Info.objects.all(),
        "src_text": src_text,
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
        "portfolio": Portfolio.objects.all(),
    }
    return render(request, "portfolio_list.html", data)

def portfolio_int_id(request, portfolio_id):
    src_text = []
    src_text.append(f"mainWindow/media/img_{portfolio_id}/im_1.png")
    src_text.append(f"mainWindow/media/img_{portfolio_id}/im_2.png")
    src_text.append(f"mainWindow/media/img_{portfolio_id}/im_3.png")
    data = {
        "title": Portfolio.title,
        "portfolio": Portfolio.objects.all()[portfolio_id - 1],
        "portfolio_id": (portfolio_id - 1),
        "src_text": src_text
    }
    return render(request, "portfolio_list_int_id.html", data)

def portfolio_str_id(request, portfolio_str):
    port_id = -1
    for i in range(len(Portfolio.objects.all())):
        if(Portfolio.objects.all()[i].title == portfolio_str):
            port_id = i
            break
    if(port_id != -1):
        src_text = []
        src_text.append(f"mainWindow/media/img_{port_id + 1}/im_1.png")
        src_text.append(f"mainWindow/media/img_{port_id + 1}/im_2.png")
        src_text.append(f"mainWindow/media/img_{port_id + 1}/im_3.png")
        data = {
            "title": Portfolio.title,
            "portfolio": Portfolio.objects.all()[port_id],
            "portfolio_id": (port_id),
            "src_text": src_text
        }
        return render(request, "portfolio_list_int_id.html", data)
    else:
        error_text = "Такого проекта у меня нет"
        data = {
            "title": "Ошибка поиска",
            "error_text": error_text,
        }
        return render(request, "errors.html", data)
