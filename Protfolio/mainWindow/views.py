from django.shortcuts import render
from django.http import HttpResponse

from .models import New
from .models import Info
from .models import Biography
from .models import Portfolio
from .models import Activity


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

def sheet_activity(request):
    data = {
        "title": "Моя учебная активность",
        "activity": Activity.objects.all(),
    }
    return render(request, "activity_list.html", data)

def activity_links(request, activity_link):
    flag = False
    act = Activity.objects.all()
    for i in act:
        if i.link == activity_link:
            flag = True
            break
    data = {
        "title": "Моя учебная активность",
        "activity": Activity.objects.all(),
    }
    if(flag):
        return render(request, "activity_list.html", data)
    else:
        error_text = "Такогой активности у меня нет"
        data = {
            "title": "Ошибка поиска",
            "error_text": error_text,
        }
        return render(request, "errors.html", data)

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
