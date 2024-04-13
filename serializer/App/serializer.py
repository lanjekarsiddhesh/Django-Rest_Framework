from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=500)
    Roll_number = serializers.IntegerField()

    def create(self, validate_data):
        '''
        Save data in db using this function
        '''
        return Student.objects.create(**validate_data)
    
    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)

        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.Roll_number = validated_data.get('Roll_number', instance.Roll_number)
        instance.save()
        return instance