from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
posts = [
    {
        'author': 'John Doe',
        'title': 'Blog Post 1',
        'content': 'First post content',
    },
    {
        'author': 'Jane Smith',
        'title': 'Blog Post 2',
        'content': 'Second post content',
    },
]
def home(request):
    context = {'posts': posts}
    return render(request,'blog/home.html', context)
def about(request):
    return render(request,'blog/about.html', {'title':'about1 title'})