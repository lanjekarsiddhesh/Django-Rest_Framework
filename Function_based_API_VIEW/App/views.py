from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *
# Create your views here.

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def Test(request,pk=None):
    if request.method == "GET":
        id = pk
        print(id)
        if id is not None:
            try:
                studn= Student.objects.get(id=id)
                studentserialize =StudentSerializer(studn)
                return Response(studentserialize.data)
            except:
                error = {"error":"Invalid ID"}
                return Response(error,status=400)
        else:
            allStudents = Student.objects.all()
            studentserialize = StudentSerializer(allStudents,many=True)
            return Response(studentserialize.data)


    if request.method == 'POST':
        data = request.data
        print(data)
        studentserialize = StudentSerializer(data=data)
        print(studentserialize)
        if studentserialize.is_valid():
            print("befpre save")
            studentserialize.save()
            print("after save")
            return Response(studentserialize.data, status=201)
        else:
            return Response(studentserialize.errors,status=400)
        
    if request.method == 'PUT' or request.method=='PATCH':
        data = request.data
        print(data['id'])
        stud = Student.objects.get(id=data.get('id'))
        serializer = StudentSerializer(stud,data=data,partial=True)
        if  serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors,status=400)

    
    if request.method == 'DELETE':
        id = pk
        try:
            stud = Student.objects.get(id=id)
            stud.delete()
            return Response(status=204)
        except Exception as e:
            error={"error":str(e)}
            return Response(error,status=400)  