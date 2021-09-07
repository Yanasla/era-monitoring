from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html') #название шаблона

def data(request):
    return render(request, 'main/data.html')