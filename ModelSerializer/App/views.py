from django.shortcuts import render
from .models import *
from .serializers import *
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.views import View
from django.http import HttpResponse, JsonResponse
from io import BytesIO

# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class StudentAPI(View):
    def get(self,request,*args,**kwargs):
        json_data = request.body
        stream = BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        if id is not None:
            data = Student.objects.get(id=id)
            serializer = StudentSerializer(data)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')

        data = Student.objects.all()
        serializer = StudentSerializer(data,many=True)
        return HttpResponse(serializer.data,content_type='application/json')
    
    def post(self,request,*args,**kwargs):
        '''
        create new record in db
        '''
        json_data = request.body
        stream = BytesIO(json_data)
        data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            res = {'msg' : f'Data created\n{serializer.data}'}
            json_res = JSONRenderer().render(res)
            return JsonResponse(serializer.data, status=201)
        json_res = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_res, content_type='application/json')
    
    def put(self,request,*args,**kwargs):
        json_data = request.body
        stream = BytesIO(json_data)
        data = JSONParser().parse(stream)
        id = data.get('id')
        Student_Model = Student.objects.get(id=id)
        # data = {'first_name': data.get('first_name'), 'last_name': data.get('last_name'), 'Roll_number': data.get('Roll_number')}
        serializer = StudentSerializer(Student_Model,data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            msg = {'msg': f'Data updated\n{serializer.data}'}
            json_res = JSONRenderer().render(msg)
            return JsonResponse(serializer.data, status=201)

        json_res = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_res, content_type='application/json')
    
    def delete(self,request,*args,**kwargs):
        json_data = request.body
        stream = BytesIO(json_data)
        data = JSONParser().parse(stream)
        id = data.get('id')
        stud = Student.objects.get(id=id).delete()
        json_re = {'msg':f'Id number {id} data is deleted'}
        json_res = JSONRenderer().render(json_re)
        return HttpResponse(json_res, content_type='application/json')