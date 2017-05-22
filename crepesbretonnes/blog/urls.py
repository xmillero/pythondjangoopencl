from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^accueil$', views.home),
    url(r'^home$', views.home),
    url(r'^article/(?P<id_article>\d+)$', views.view_article),
    url(r'^article/(?P<id_categorie>\d+)$', views.view_article),
    url(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})$', views.list_articles),
    url(r'^date', views.date_actuelle),
    url(r'^addition/(?P<nombre1>\d+)/(?P<nombre2>\d+)/$', views.addition),
    url(r'^contact/$', views.contact, name='contact'),
    ]