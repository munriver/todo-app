# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.middleware.csrf import get_token

from todoapp.models import Task
from todoapp.serializers import TaskSerializer
from rest_framework import generics 
from rest_framework import permissions 
from todoapp.permissions import IsOwnerOrReadOnly

# Create your views here.


class TaskList(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    def get_queryset(self):
        return Task.objects.filter(Q(author=self.request.user.id) 
                                   | Q(private=False))

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, 
                          IsOwnerOrReadOnly,)


def csrf(request):
    return JsonResponse({'csrfToken': get_token(request)})


def current_user(request):
    return JsonResponse({'username': request.user.username}) 
