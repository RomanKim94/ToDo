from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Task
from .permissions import AdminOrOwnTaskPermission
from .serializers import TaskListSerializer, TaskDetailSerializer
from lists.models import List

from .services import TaskServices


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer
    permission_classes = (IsAuthenticated, AdminOrOwnTaskPermission)

    def get_serializer_class(self):
        if self.action == 'list':
            return TaskListSerializer
        return TaskDetailSerializer

    def get_queryset(self):
        qs = Task.objects.all()
        person = self.request.user
        qs = TaskServices.qs_filter(qs, self.request.query_params, person)
        qs = TaskServices.qs_sorting(qs, self.request.query_params)

        return qs

    def create(self, request, *args, **kwargs):
        current_user = self.request.user
        general_list = List.objects.filter(person=current_user, name='General').first()
        if not general_list:
            List.objects.create(person=current_user, name='General')
        new_data = dict(request.data.items())
        print(new_data.items())
        new_data.setdefault('list', List.objects.filter(person=current_user, name='General').first().id)
        serializer = self.get_serializer(data=new_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
