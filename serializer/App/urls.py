from django.urls import path
from .views import *

urlpatterns = [
    path('StudentAPI',StudentAPI.as_view()),
    path('GetStudentData', student_detail),
    path('Store',student_create),
    path('Update',student_update),
    path('Delete',student_delete)
]
