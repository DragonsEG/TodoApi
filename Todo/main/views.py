from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from . serializers import *
from . models import Task

# Create your views here.


##def index(request):
  ##  return HttpResponse('Hello world')

class TodoList(generics.ListAPIView):
    queryset=Task.objects.all()
    serializer_class=Todo

class TaskDetails(generics.RetrieveUpdateAPIView):
    queryset=Task.objects.all()
    serializer_class=Todo

class CreateTask(generics.CreateAPIView):
    queryset=Task.objects.all()
    serializer_class=Todo

class DeleteTask(generics.DestroyAPIView):
     queryset=Task.objects.all()
     serializer_class=Todo

class filter(generics.ListAPIView):
    queryset=Task.objects.all()
    serializer_class=Todo
    def get_queryset(self):
        return Task.objects.filter(iscomplete=True)
    
class search(generics.ListAPIView):
    queryset=Task.objects.all()
    serializer_class=Todo
    def get_queryset(self):
        queryset=Task.objects.all()
        title=self.request.query_params.get('title')
        if title is not None:
            queryset=queryset.filter(title=title)
            return queryset