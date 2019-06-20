from django.shortcuts import render
from django.http import HttpResponse
from . models import Post


def home(request):
    context = {
        'posts' : Post.objects.all(),
        'title' : 'Home Page'
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title' : 'about'})


def contacts(request):
    context = {
        'name' : 'egis1',
    }
    return render(request, 'blog/contacts.html', context)