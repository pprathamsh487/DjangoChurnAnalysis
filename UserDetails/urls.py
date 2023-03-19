from django.urls import path
from . import views

urlpatterns = [
    path('getDetails/', views.getDetails, name = 'index')
]
