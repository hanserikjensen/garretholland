from django.conf.urls import url
from . import views

app_name = 'survey_form'
urlpatterns = [
    url(r'^result/$', views.result, name='result'),
    url(r'^surveys/process$', views.survey, name='survey'),
    url(r'^$', views.index, name='index')
    ]
