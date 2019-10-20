from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'joe',
        'title': 'blog post 1',
        'content': 'First post content',
        'date_posted':"August 27, 2018"
    },{
        'author': 'jane',
        'title': 'blog post 2',
        'content': 'Second post content',
        'date_posted':"August 28, 2018"
    }
]
def home(request):
    context = {
        'posts':posts,
        'title':'Tillog Home'
    }
    return render(request, 'blog/home.html', context)

def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'blog/about.html', context)
