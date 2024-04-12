from django.urls import path
from .views import *

urlpatterns = [
    path('GetStudentData', student_detail),
    path('Store',student_create)
]
