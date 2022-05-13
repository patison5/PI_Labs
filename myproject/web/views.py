from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

posts = [
    {
        'author': 'holey',
        'title': 'shit',
        'description': 'is',
        'text': 'that shit!?'
    },
    {
        'author': 'that',
        'title': 'is',
        'description': 'unbelievable',
        'text': 'shit!'
    }
]

# Create your views here.
def index(request):
    context = {
        'posts': posts
    } 
    return render(request, 'web/index.html', context)

def about(request):
    return JsonResponse({'foo':'bar'})