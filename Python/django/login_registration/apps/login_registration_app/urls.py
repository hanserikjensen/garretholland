from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^create_comment/(?P<course_id>\d+)$',views.create_comment),
    # url(r'^courses/destroy/destroy_course/(?P<course_id>\d+)$', views.destroy_course),
    # url(r'^destroy_course/(?P<course_id>\d+)$', views.destroy_course),
    # url(r'^courses/destroy/(?P<course_id>\d+)$', views.destroy_course),
    url(r'^success$', views.success),
    url(r'^register$', views.process),
    url(r'^login$', views.process),
    url(r'^$', views.index),
    ]
