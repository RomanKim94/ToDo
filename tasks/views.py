from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Task
from .permissions import AdminOrOwnTaskPermission
from .serializers import TaskListSerializer, TaskDetailSerializer
from lists.models import List


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer
    permission_classes = (IsAuthenticated, AdminOrOwnTaskPermission)

    def get_serializer_class(self):
        if self.action != 'list':
            return TaskDetailSerializer
        return TaskListSerializer

    def get_queryset(self):
        qs = Task.objects.all()
        if not self.request.user.is_staff:
            qs = qs.filter(list__person=self.request.user)
        return qs

    def create(self, request, *args, **kwargs):
        request.data.setdefault('list', List.objects.filter(person=self.request.user, name='General').first().id)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
