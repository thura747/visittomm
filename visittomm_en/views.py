from django.shortcuts import render

# Create your views here.

from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.views.generic.edit import FormView
from django.template import Context, Template, RequestContext, loader
import json

from .models import Post2

from .models import Cities, RegionsStates, Destinations

# def post_list(request):
#     return render(request, 'blog/post_list.html', {})


class Index(View):
    # def get(self, request):
    #     return HttpResponse('I am called from a get Request')

    def get(self, request):
        params = {}
        params["name"] = "Django"
        posts = Post2.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        params["post"] = posts

        destinations = Destinations.objects.order_by('id')[:9]
        params["destinations"] = destinations
        return render(request, 'en/index.html', {'destinations': destinations})

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



from django.template import RequestContext
def ajax_mymodel_list(request):
    """ returns data displayed at autocomplete list -
    this function is accessed by AJAX calls
    """
    limit = 10
    query = request.GET.get('q', None)
    # it is up to you how query looks
    if query:
        qargs = [django.db.models.Q(name__istartswith=query)]

    instances = Cities.objects.filter(django.db.models.Q(*qargs))[:limit]

    results = ""
    for item in instances:
        results += "%s|%s \n" %(item.pk,item.name)

    return HttpResponse(results)