from django.shortcuts import render

# Create your views here.

from django.utils import timezone
from django.shortcuts import render, get_object_or_404

from .models import Post2


# def post_list(request):
#     return render(request, 'blog/post_list.html', {})

def post_list(request):
    posts = Post2.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'en/post_list.html', {'posts': posts})


def post_detail(request, pk):
    # post = get_object_or_404(Post2, pk=pk)
    return render(request, 'en/post_detail.html')
