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
    return render(request, 'polls/home.html', context)

def about(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    # context = {
    #     'posts': posts
    # } 
    # return render(request, 'polls/elements.html', context)
    return JsonResponse({'foo':'bar'})