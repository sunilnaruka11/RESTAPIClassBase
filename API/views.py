from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import status
from django.http import Http404
# class  based views.
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializer import TaskSerializer 
from .models import Task   

class TaskList(APIView):
    """
    List all Task, or create a new snippet.
    """
	
    def get(self, request, format=None):
        taskdata = Task.objects.all()
        serializer = TaskSerializer(taskdata, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)           

class TaskDetail(APIView):
    """
    Retrieve, update or delete a Task instance.
    """
    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        taskdata = self.get_object(pk)
        serializer = TaskSerializer(taskdata)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        taskdata = self.get_object(pk)
        serializer = TaskSerializer(taskdata, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        taskdata = self.get_object(pk)
        taskdata.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)