from django.shortcuts import render
#from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def index(request):
    return HttpResponse('Home Page')

def userInterface(request):
    cname = 'Medha'
    Duration = '2 years'
    seats = '150'
    d = datetime.now()

    UI_list = {'cn':cname, 'du': Duration, 'st': seats, 'dt': d}
   # new_list = {'new': cname, 'time': Duration, 'seat': seats}
    return render(request, 'UI_files/mainUI.html', context =  UI_list)
