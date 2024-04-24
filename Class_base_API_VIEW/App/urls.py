from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('StudentAPI', StudentAPI.as_view()),
    path('StudentAPI/<int:pk>', StudentAPI.as_view())
]