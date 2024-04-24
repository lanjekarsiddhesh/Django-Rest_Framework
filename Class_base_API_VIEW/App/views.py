from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views  import APIView
from .models import *
from .serializer import *

# Create your views here.
class StudentAPI(APIView):
    def get(self,request,pk=None,format=None):
        id = pk
        if id is not None:
            try:
                stud = Student.objects.get(id=id)
                serializer = StudentSerializer(stud)
                return Response(serializer.data)
            except:
                return Response("Student with this ID does not exist")
        else:
            stud = Student.objects.all()
            serializer = StudentSerializer(stud, many=True)
            return Response(serializer.data)

    def post(self, request,format=None):
        data = request.data
        seria = StudentSerializer(data=data)
        if seria.is_valid():
            seria.save()
            return Response("Student Successfully Created")
        else:
            return Response(seria.errors)
        
    def patch(self,request,format=None):
        data = request.data
        stud = Student.objects.get(id=data.get('id'))
        seria = StudentSerializer(stud,data=data,partial=True)
        if seria.is_valid():
            seria.save()
            return Response("Student Details Updated Succesfully")
        else:
            return Response(seria.errors)
        
    def delete(self,request,pk=None,format=None):
        id = pk
        print(id)
        try:
            stud = Student.objects.get(pk=id)
            stud.delete()
            return Response(f"The student record has been deleted successfully.")
        except Exception as e:
            return Response(str(e))

