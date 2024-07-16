from API import views
from django.urls import path

urlpatterns = [
    path('API_views/', views.api_view),
]