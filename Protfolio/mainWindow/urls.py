from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("biography/", views.sheet_biography, name="biography"),
    path("portfolio_list/", views.portfolio_list, name="portfolio_list"),
]