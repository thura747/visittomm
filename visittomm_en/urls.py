from django.conf.urls import url
from . import views

# Standard
from visittomm_en.views import Index, Contact

# Trips/Destinations
from visittomm_en.views import Trips, TripDetail
from visittomm_en.views import DestinationsList, DestinationDetail, DestinationsListByRegion, DestinationsListByCity



urlpatterns = [
    # url(r'^en/$', views.post_list, name='post_list'),

    url(r'^en/$', Index.as_view()),
    url(r'^en/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^en/trips/$', Trips.as_view()),
    url(r'^en/trip-detail/$', TripDetail.as_view()),
    url(r'^en/contact/$', Contact.as_view()),
    url(r'^en/destinations/$', DestinationsList.as_view()),
    url(r'^en/destinations/detail/(?P<pk>\d+)/$', DestinationDetail.as_view()),
    url(r'^en/destinations/country/(\w+)/$', DestinationsList.as_view()),
    url(r'^en/destinations/regional/(\w+)/$', DestinationsListByRegion.as_view()),
    url(r'^en/destinations/city/(\w+)/$', DestinationsListByCity.as_view()),

    url(r'^api/get_cities/', views.get_cities, name='get_cities'),
]