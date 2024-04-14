from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from .models import *
from .serializer import *

import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from django.utils.decorators import method_decorator
from django.views import View


# Create your views here.

#-------------------------------------------------Class based view--------------------------------------------------------------
@method_decorator(csrf_exempt,name='dispatch')
class StudentAPI(View):
    def get(self,request,*args,**kwargs):
        '''
        fetch all db record and covert into json object and return
        '''
        JSON_DATA = request.body
        stream = io.BytesIO(JSON_DATA)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id',None)
        if id is not None:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student)
            JSON_DATA = JSONRenderer().render(serializer.data)
            return HttpResponse(JSON_DATA,content_type='application/json')
            

        student_data = Student.objects.all()
        serializer_data = StudentSerializer(student_data,many=True)
        return JsonResponse(serializer_data.data, safe=False)
    
    def post(self,request,*args,**kwargs):
        '''
        create new record in db
        '''
        json_data = request.body
        stream = io.BytesIO(json_data)
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
        '''
        update record in db
        '''
        json_data = request.body
        stream = io.BytesIO(json_data)
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
        '''
        delete record in db
        '''
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        id = data.get('id')
        Student_Model = Student.objects.get(id=id)
        Student_Model.delete()
        msg = {'msg': f'Data of id {id} deleted'}
        json_res = JSONRenderer().render(msg)
        return HttpResponse(json_res, content_type='application/json')



#-------------------------------------------------Function based view--------------------------------------------------------------

def student_detail(request):
    '''
    fetch all db record and covert into json object and return
    '''
    if request.method == 'GET':
        JSON_DATA = request.body
        stream = io.BytesIO(JSON_DATA)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id',None)
        if id is not None:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student)
            JSON_DATA = JSONRenderer().render(serializer.data)
            return HttpResponse(JSON_DATA,content_type='application/json')
            

        student_data = Student.objects.all()
        serializer_data = StudentSerializer(student_data,many=True)
        # json_data = JSONRenderer().render(serializer_data.data)
        # return HttpResponse(json_data, content_type='application/json')
        return JsonResponse(serializer_data.data, safe=False)

@csrf_exempt
def student_create(request):
    '''
    create new record in db
    '''
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=data)

        # data = JSONParser().parse(request)
        # serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg' : f'Data created\n{serializer.data}'}
            json_res = JSONRenderer().render(res)
            return JsonResponse(serializer.data, status=201)
            # return HttpResponse(json_res, content_type='application/json')
        json_res = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_res, content_type='application/json')

        # return JsonResponse(serializer.errors, status=400)

@csrf_exempt   
def student_update(request):
    '''
    update record in db
    '''
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        id = data.get('id')
        Student_Model = Student.objects.get(id=id)
        serializer = StudentSerializer(Student_Model,data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            msg = {'msg': f'Data updated\n{serializer.data}'}
            json_res = JSONRenderer().render(msg)
            # return HttpResponse(json_res, content_type='application/json')
            return JsonResponse(serializer.data, status=201)

        json_res = JSONRenderer().render(serializer.errors)
        # return HttpResponse(json_res, content_type='application/json')
        return JsonResponse(json_res, status=400)

@csrf_exempt     
def student_delete(request):
    '''
    delete record in db
    '''
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        id = data.get('id')
        Student_Model = Student.objects.get(id=id)
        Student_Model.delete()
        msg = {'msg': f'Data of id {id} deleted'}
        json_res = JSONRenderer().render(msg)
        return HttpResponse(json_res, content_type='application/json')
    msg = {'msg':"Choose delete not other"}
    return JsonResponse(msg, status=400)
   