from django.urls import path
from properties import views


urlpatterns = [
    path('', views.homepage)
]