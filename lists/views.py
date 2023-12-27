from django.shortcuts import render
from rest_framework import viewsets

from ToDoList.lists.models import List
from ToDoList.lists.permissions import OwnListPermission
from ToDoList.lists.serializers import ListListSerializer, ListDetailSerializer


class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListListSerializer
    permission_classes = OwnListPermission

    def get_serializer_class(self):
        if self.action != 'list':
            return ListDetailSerializer
        return ListListSerializer
