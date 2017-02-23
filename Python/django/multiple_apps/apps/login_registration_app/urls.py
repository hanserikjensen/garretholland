from django.conf.urls import url
from . import views

#login_register:success

app_name = 'login_register'
urlpatterns = [
    url(r'^courses/$', views.redirect, name='courses'),
    url(r'^success/$', views.success, name='success'),
    url(r'^register/$', views.process, name='register'),
    url(r'^login/$', views.process, name='login'),
    url(r'^process/$', views.process, name='login'),
    url(r'^$', views.index, name='index'),
    ]
