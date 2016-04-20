from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^en/$', views.post_list, name='post_list'),
    url(r'^en/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]