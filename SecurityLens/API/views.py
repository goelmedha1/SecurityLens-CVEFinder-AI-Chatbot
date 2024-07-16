from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def api_view(request):
    return HttpResponse('this is for APIs')
