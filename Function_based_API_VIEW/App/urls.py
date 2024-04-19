from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('test', Test),
    path('test/<int:pk>', Test)
]