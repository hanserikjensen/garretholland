from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^success$', views.success),
    url(r'^register$', views.process),
    url(r'^login$', views.process),
    url(r'^$', views.index),
    ]
