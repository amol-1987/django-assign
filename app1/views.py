from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSeri
from .models import Task
# Create your views here.
@api_view(['GET'])
def api(request):
	api_urls = {
		'list':'/tasklist/',
		'detail':'/taskdetail/',
		}
	return Response(api_urls)
	
@api_view(['GET'])
def tasklist(request):
	tasks=Task.objects.all()
	serializer = TaskSeri(tasks, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def taskdetail(request,pk):
	tasks=Task.objects.get(id=pk)
	serializer = TaskSeri(tasks, many=False)
	return Response(serializer.data)