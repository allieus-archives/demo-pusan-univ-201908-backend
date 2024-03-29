# univ/urls.py
from django.urls import path
from . import views

app_name = 'univ'

urlpatterns = [
    path('professor/', views.professor_list),
    path('professor.json', views.professor_list_json),
]
