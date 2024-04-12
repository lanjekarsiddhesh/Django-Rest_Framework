from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=500)
    Roll_number = serializers.IntegerField()

    def create(self, validate_data):
        return Student.objects.create(**validate_data)