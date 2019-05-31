from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author' : 'Egis',
        'title' : 'Blog Post 1',
        'content' : 'First post ever',
        'date_posted' : 'August 27, 1998',
    },
    {
        'author' : 'Jane',
        'title' : 'Blog Post 2',
        'content' : 'Second post ever',
        'date_posted' : 'September 27, 2005',
    } 
]

def home(request):
    context = {
        'posts' : posts,
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