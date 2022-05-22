from django.shortcuts import render
from rest_framework import viewsets, generics, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import OrderingFilter, SearchFilter

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action, api_view

from django.contrib.auth.models import User
from .serializers import TaskSerializer
from .models import Task
from .paginations import CustomPagination
# Create your views here.


class TaskViewSet(viewsets.ViewSet, generics.ListAPIView, generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetailViewSet(generics.RetrieveDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
