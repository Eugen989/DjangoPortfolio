from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path("activity/", views.sheet_activity, name="activity"),
    #path("activity_id/<slug:activity_link>", views.activity_links, name="activity_views"),
    path("activity_links/<slug:activity_link>", views.activity_links, name="activity_links"),
    path("biography/", views.sheet_biography, name="biography"),
    path("portfolio_list/", views.portfolio_list, name="portfolio_list"),
    path("portfolio_list/<int:portfolio_id>", views.portfolio_int_id, name="portfolio_int_id"),
    path("portfolio_list/<slug:portfolio_str>", views.portfolio_str_id, name="portfolio_str_id"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)