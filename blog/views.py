from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'coreyMs',
        'title': 'blog post 1',
        'content': 'First post content',
        'date_posted': 'August 19 2018'
    },
    {
        'author': 'Bob ross',
        'title': 'blog post 2',
        'content': 'Second post content',
        'date_posted': 'August 21 2018'
    }
]


# Create your views here.
def home(request):
    context ={
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html',{ 'title': 'About'})
