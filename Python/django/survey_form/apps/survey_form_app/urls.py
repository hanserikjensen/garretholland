from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^result$', views.result),
    url(r'^surveys/process$', views.survey),
    url(r'^$', views.index)
    ]
