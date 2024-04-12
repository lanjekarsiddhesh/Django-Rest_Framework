from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from .models import *
from .serializer import *

import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def student_detail(request):
    '''
    fetch all db record and covert into json object and return
    '''
    student_data = Student.objects.all()
    serializer_data = StudentSerializer(student_data,many=True)
    # json_data = JSONRenderer().render(serializer_data.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer_data.data, safe=False)

@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=data)

        # data = JSONParser().parse(request)
        # serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg' : 'Data created'}
            json_res = JSONRenderer().render(res)
            # return JsonResponse(serializer.data, status=201)
            return HttpResponse(json_res, content_type='application/json')
        json_res = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_res, content_type='application/json')

        # return JsonResponse(serializer.errors, status=400)
    