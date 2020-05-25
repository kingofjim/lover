from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    print('haha')
    return render(request, 'index.html', {})

def apply(request):
    return render(request, 'apply.html', {})