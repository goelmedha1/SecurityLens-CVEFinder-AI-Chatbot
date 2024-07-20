from UI import views
from django.urls import path

urlpatterns = [
    path('UserInterface/', views.userInterface),
    #path('UserInterface/', views.showformdata),
]