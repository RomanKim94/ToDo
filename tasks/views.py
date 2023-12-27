from django.shortcuts import render
from rest_framework import viewsets

from .models import Task
from .permissions import AdminOrOwnTaskPermission
from .serializers import TaskListSerializer, TaskDetailSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer
    permission_classes = (AdminOrOwnTaskPermission, )

    def get_serializer_class(self):
        if self.action != 'list':
            return TaskDetailSerializer
        return TaskListSerializer
