from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

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

def index(request):
    return HttpResponse("Hello, world. You're at the /api index page.")

def profiles(request):
    return JsonResponse({'profiles': posts})

def products(request):
    return JsonResponse({'products': posts})

def categories(request):
    return JsonResponse({'categories': posts})