from django.urls import path
from . import views

#localhost:8000/chatbot
#Control takein from main project urls.py file. 
#Now if you want to add further urs you can just add the next ones like /details etc. 

urlpatterns = [
    path('cve_chatbot/', views.cve_chatbot, name="cve_chatbot"),   
]
