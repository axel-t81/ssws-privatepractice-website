from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('costing/', views.costing, name='costing'),
    path('resources/', views.resources, name='resources'),
]