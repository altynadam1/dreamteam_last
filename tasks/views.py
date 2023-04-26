from django.shortcuts import render
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import permissions

from .models import Task
from .serializers import TaskSerializers
from .permissions import IsOwnerOrReadOnly


class TaskListAPIView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = ['title']
    search_fields = ['title']


class TaskCreateAPIView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class TaskAPIRetriveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers 
    permission_classes = [IsOwnerOrReadOnly]

