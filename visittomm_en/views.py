from django.shortcuts import render

# Create your views here.

from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.views.generic.edit import FormView
from django.template import Context, Template, RequestContext, loader
import json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from .models import Post2

from .models import Cities, RegionsStates, Destinations, Packages

from visittomm_en.forms import IndexSearchTripForm

# def post_list(request):
#     return render(request, 'blog/post_list.html', {})


class Index(View):
    # def get(self, request):
    #     return HttpResponse('I am called from a get Request')

    def get(self, request):
        params = {}
        search_form = IndexSearchTripForm()

        destinations = Destinations.objects.order_by('id')[:9]
        params["destinations"] = destinations
        params["current_menu"] = 'Index'
        params["search_trip_form"] = search_form
        return render(request, 'en/index.html', params)

    def post(self, request):
        origin = request.POST['origin']
        destinations = request.POST['destinations']
        return HttpResponseRedirect('/en/trip/search/' + origin + "/" + destinations)

        # form = IndexSearchTripForm(self.request.POST)
        # if form.is_valid():
        #     # user = User.objects.get(username=username)
        #     # tweet = Tweet(text=form.cleaned_data['text'],
        #     #               user=user,
        #     #               country=form.cleaned_data['country'])
        #     # tweet.save()
        #     words = form.cleaned_data['text'].split(" ")
        #     for word in words:
        #         if word[0] == "#":
        #             hashtag, created = HashTag.objects.get_or_create(name=word[1:])
        #             hashtag.tweet.add(tweet)
        # return HttpResponseRedirect('/user/' + username)

class TripsList(View):
    def get(self, request, origin, destinations):

        import pdb
        pdb.set_trace()
        print origin
        print destinations
        return render(request, 'en/contact.html', {'current_menu': current_menu})



class Contact(View):

    def get(self, request):
        current_menu = 'Contact'
        return render(request, 'en/contact.html', {'current_menu': current_menu})

    def post(self, request):
        return HttpResponse('I am called from a post Request')


class DestinationsList(View):

    def get(self, request):
        params = {}
        destinations = Destinations.objects.all().order_by('id')
        paginator = Paginator(destinations, 10)  # Show 10 contacts per page

        page = request.GET.get('page')
        try:
            destinations = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            destinations = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            destinations = paginator.page(paginator.num_pages)

        params["destinations"] = destinations
        params["page_cnt"] = range(1, paginator.num_pages + 1)
        params["current_menu"] = 'Destinations'
        params["breadcrumb"] = "country"
        return render(request, 'en/destinations/destination_list.html', params)

    def post(self, request):
        return HttpResponse('I am called from a post Request')


class DestinationsListByCity(View):

    def get(self, request, city_name):
        params = {}
        try:
            city = Cities.objects.get(name=city_name)
        except Cities.DoesNotExist:
            raise Http404('"' + city_name + '" city does not exist')

        regions_states = RegionsStates.objects.get(id=city.id)
        destinations = Destinations.objects.filter(region_id=regions_states.id)
        paginator = Paginator(destinations, 10)  # Show 25 contacts per page

        page = request.GET.get('page')
        try:
            destinations = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            destinations = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            destinations = paginator.page(paginator.num_pages)

        params["destinations"] = destinations
        params["page_cnt"] = range(1, paginator.num_pages + 1)
        params["current_menu"] = 'Destinations'
        params["breadcrumb"] = "city"
        params["city_name"] = city.name
        params["region"] = regions_states.name
        return render(request, 'en/destinations/destination_list.html', params)

    def post(self, request):
        return HttpResponse('I am called from a post Request')


class DestinationsListByRegion(View):

    def get(self, request, region_name):
        params = {}

        try:
            regions_states = RegionsStates.objects.get(name=region_name)
        except RegionsStates.DoesNotExist:
            raise Http404('"' + region_name + '" region does not exist')

        destinations = Destinations.objects.filter(region_id=regions_states)


        paginator = Paginator(destinations, 10)  # Show 25 contacts per page

        page = request.GET.get('page')
        try:
            destinations = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            destinations = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            destinations = paginator.page(paginator.num_pages)

        params["destinations"] = destinations
        params["page_cnt"] = range(1, paginator.num_pages + 1)
        params["current_menu"] = 'Destinations'
        params["breadcrumb"] = "region"
        params["region"] = regions_states.name
        return render(request, 'en/destinations/destination_list.html', params)

    def post(self, request):
        return HttpResponse('I am called from a post Request')


class DestinationDetail(View):

    def get(self, request, pk):
        destinations = get_object_or_404(Destinations, id=pk)
        current_menu = 'Destinations'
        return render(request, 'en/destinations/destinations_detail.html',
                      {'destinations': destinations, 'current_menu': current_menu})

    def post(self, request):
        return HttpResponse('I am called from a post Request')

def post_list(request):
    posts = Post2.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'en/post_list.html', {'posts': posts})


def post_detail(request, pk):
    # post = get_object_or_404(Post2, pk=pk)
    return render(request, 'en/post_detail.html')


def get_cities(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        if q is None:
            cities = Cities.objects.order_by('region_id')

        else:
            cities = Cities.objects.filter(name__icontains=q).order_by('region_id')
        results = []

        for i in range(0, len(cities)):
            city_json = {}
            city_json['id'] = cities[i].id
            city_json['label'] = cities[i].name
            city_json['category'] = cities[i].region_id.name
            results.append(city_json)
        data = json.dumps(results)
    else:
        data = 'fail'

    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


class Trips(View):
    def get(self, request, origin, destinations):
        params = {}
        try:
            origin_city = Cities.objects.get(name=origin)
        except Cities.DoesNotExist:
            raise Http404('"' + origin + '" city does not exist')

        try:
            destinations_city = Cities.objects.get(name=destinations)
        except Cities.DoesNotExist:
            raise Http404('"' + destinations + '" city does not exist')

        regions_states = RegionsStates.objects.get(id=destinations_city.region_id.id)
        trips = Packages.objects.filter(origin=origin_city.id, destination=destinations_city.id)

        paginator = Paginator(trips, 10)  # Show 25 contacts per page

        page = request.GET.get('page')
        try:
            trips = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            trips = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            trips = paginator.page(paginator.num_pages)

        params["trips"] = trips
        params["page_cnt"] = range(1, paginator.num_pages + 1)
        params["current_menu"] = 'Trips'
        params["breadcrumb"] = "city"
        params["region"] = regions_states.name
        params["city_name"] = destinations_city.name

        return render(request, 'en/destinations/trips.html', params)

    def post(self, request):
        return HttpResponse('I am called from a post Request')


class TripDetail(View):
    def get(self, request, pk):
        params = {}
        params["trips"] = get_object_or_404(Packages, id=pk)
        params["current_menu"] = 'Trips'
        return render(request, 'en/destinations/trip_detail.html', params)
