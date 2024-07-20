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
    # if request.method == "GET" and "q" in request.GET:
    #     query = request.GET["q"]
    #     results = call_openai_api(query)
    #     return JsonResponse({'results': results})
    fm = UI_form()
    return render(request, 'UI_files/mainUI.html', {'forms':fm})
    #return render(request, 'UI_files/mainUI.html')

# def call_openai_api(query):
#     response = openai.Completion.create(
#         engine="text-davinci-003",
#         prompt=query,
#         max_tokens=100
#     )

#     return response.choices[0].text.strip()

def QuerySearch(request):
    sq = SearchQuery.objects.all()
    return(request, 'UI_files/mainUI.html', {'squery': sq})


# def showformdata(request):
#     fm = UI_form()
#     return render(request, 'UI_files/mainUI.html', {'forms':fm})


