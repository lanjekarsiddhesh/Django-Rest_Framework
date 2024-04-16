from django.urls import path
from .views import *

urlpatterns = [
    path('StudentAPI',StudentAPI.as_view()),
]