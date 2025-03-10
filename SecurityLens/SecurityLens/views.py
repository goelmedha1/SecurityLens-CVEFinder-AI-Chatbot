from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("Hello World, you are at SecurityLense home page")
    return render(request, 'website/index.html')

def contact(request):
    return HttpResponse("Hello World, you are at SecurityLense contact page")

def about(request):
    return HttpResponse("Hello World, you are at SecurityLense about page")
