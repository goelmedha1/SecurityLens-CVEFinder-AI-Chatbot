from django.shortcuts import render
#from django.http import HttpResponse
#import openai
from django.http import JsonResponse
from django.conf import settings
from UI.models import SearchQuery
from .forms import UI_form


# openai.api_key = settings.OPENAI_API_KEY
# Create your views here.

def index(request):
    return HttpResponse('Home Page')

def userInterface(request):

    if request.method == 'POST':
        fm = UI_form(request.POST)
        if fm.is_valid():
            
            query =  fm.cleaned_data['search_box']
            db_data = SearchQuery(id = None, search_box=query)
            db_data.save()

    else:
        fm = UI_form()
    return render(request, 'UI_files/mainUI.html', {'forms':fm})  

    #return render(request, 'UI_files/mainUI.html')




# def showformdata(request):
#     fm = UI_form()
#     return render(request, 'UI_files/mainUI.html', {'forms':fm})


