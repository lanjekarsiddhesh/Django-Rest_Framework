from rest_framework import serializers
from .models import *
import re


class StudentSerializer(serializers.ModelSerializer):
    def roll_gt_and_lt(value):   
        if value > 200 or value <0:
            raise serializers.ValidationError("Roll number can not be Zero or more than 100")
    Roll_number = serializers.IntegerField(validators=[roll_gt_and_lt])
    class Meta:
        model = Student

        fields = ['first_name','last_name','Roll_number']
        # exclude = ['id']
        # read_only_fields = ['Roll_number']

    def validate_first_name(self, value):
        if not re.match("^[a-zA-Z]*$", value):
            raise serializers.ValidationError("Invalid characters in the field only alphabets are valid characters")
        
        return value
        
