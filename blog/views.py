from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from blog.models import Blogpost


def index(request):
    # we are storing oll objects of the blogpost in a variable name myposts
    myposts = Blogpost.objects.all()
    print(myposts)
    return render(request, 'blog/index.html', {'myposts': myposts})


def blogpost(request, id):
    post = Blogpost.objects.filter(post_id=id)[0]
    print(post)
    return render(request, 'blog/blogpost.html', {'post': post})
