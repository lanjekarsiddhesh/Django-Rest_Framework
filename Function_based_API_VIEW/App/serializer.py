from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Student
        fields = ['id','first_name','last_name','Roll_number']