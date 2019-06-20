# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from todoapp.models import Task
from todoapp.serializers import TaskSerializer
from rest_framework import generics 
from rest_framework import permissions 

# Create your views here.


class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
