from django.shortcuts import render

# Create your views here.

from django.contrib.auth import get_user_model
from .models import Task, Comment, Project
from .serializers import TaskSerializer, ProjectSerializer, CommentSerializer
from rest_framework.views import APIView
from rest_framework import viewsets


User = get_user_model()


class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class ProjectView(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

