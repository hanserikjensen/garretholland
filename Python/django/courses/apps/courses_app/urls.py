from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^delete_email/(?P<user_id>\d+)$', views.delete_link),
    url(r'^create$', views.create_course),
    url(r'^$', views.index)
    ]
