from rest_framework import serializers
from .models import *
import re

#validator
def roll_gt_and_lt(value):
    '''
    This method is validator used for of the 'roll_number' field.
    This method validate the roll number value is not less than 0 or not greater than 200 then it will pass otherwise it will give throw error.
    if we intialize the seriliazer field in the field we implement this validator ex. validators=function_name;
    This validator refers to validating specific fields in a serializer
    If any error occur then it will show the error message,
    This validator write the outside of serilaizer class.
    this vaildator is first priority.
    '''
    if value > 200 or value <0:
        raise serializers.ValidationError("Roll number can not be Zero or more than 100")
     
#seriliazer   
class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=500)
    Roll_number = serializers.IntegerField(validators=[roll_gt_and_lt])

    def create(self, validate_data):
        '''
        Save data in db using this function
        '''
        return Student.objects.create(**validate_data)
    
    def update(self, instance, validated_data):
        '''
        Update data in dbusing this function
        '''
        instance.id = validated_data.get('id', instance.id)

        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.Roll_number = validated_data.get('Roll_number', instance.Roll_number)
        instance.save()
        return instance
    
    #Field level validation
    """
    def validate_first_name(self, value):
        '''
        This method is  used for field-level validation of the 'first_name' field.
        This method validate the only string contains any special character then it will give throw error otherwise it will pass.
        This validation method call FIELD LEVEL VALIDATION method;
        Field-level validation refers to validating individual fields in a serializer
        If any error occur then it will show the error message,
        field-level validation is second priority.
        '''
        if not re.match("^[a-zA-Z]*$", value):
            raise serializers.ValidationError("Invalid characters in the field only alphabets are valid characters")
        
        return value
    
    def validate_last_name(self, value):
        '''
        This method is  used for field-level validation of the 'last_name' field.
        This method validate the only string contains any special character then it will give throw error otherwise it will pass.
        This validation method call FIELD LEVEL VALIDATION method;
        Field-level validation refers to validating individual fields in a serializer
        If any error occur then it will show the error message,
        field-level validation is second priority.
        '''
        if not re.match("^[a-zA-Z]*$", value):
            raise serializers.ValidationError("Invalid characters in the field only alphabets are valid characters")
        
        return value
    
    def validate_Roll_number(self, value):
        '''
        This method is  used for field-level validation of the 'Roll_number' field.
        This method validate the roll number value is not less than 0 or not greater than 200 then it will pass otherwise it will give throw error.
        This validation method call FIELD LEVEL VALIDATION method;
        Field-level validation refers to validating individual fields in a serializer
        If any error occur then it will show the error message,
        field-level validation is second priority.
        '''
        if value > 200 or value <= 0:
            raise serializers.ValidationError("Roll number can not be Zero or more than 100")
        
        if not str(value).isdigit():
            raise serializers.ValidationError("Roll number contains only numbers not a other characters")
        
        return value
   
    """

    #Global validation
    def validate(self, data):
        '''
        This validation method call GLOBAL VALIDATION method;
        Global validation refers to validating the entire request data, typically in the serializer's validate method.
        If any error occur then it will show the error message,
        Global validation is last priority.
        '''
        f_name = data.get('first_name')
        l_name = data.get('last_name')
        # roll = data.get('Roll_number')

        if not re.match("^[a-zA-Z]*$",f_name):
            raise serializers.ValidationError("Invalid characters in the field only alphabets are valid characters")
        
        if not re.match("^[a-zA-Z]*$",l_name):
            raise serializers.ValidationError("Invalid characters in the field only alphabets are valid characters")
        '''
        if roll > 200 or roll <= 0:
            raise serializers.ValidationError("Roll number can not be Zero or more than 100")
            '''
        
        return data
        
