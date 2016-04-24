from django.conf.urls import url
from . import views

from visittomm_en.views import Index


urlpatterns = [
    # url(r'^en/$', views.post_list, name='post_list'),

    url(r'^en/$', Index.as_view()),
    url(r'^en/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),


    url(r'^api/get_cities/', views.get_cities, name='get_cities'),

]