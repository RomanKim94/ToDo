from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import List
from .permissions import OwnListPermission
from .serializers import ListListSerializer, ListDetailSerializer


class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListListSerializer
    permission_classes = (
        OwnListPermission,
        IsAuthenticated
    )

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ListDetailSerializer
        return ListListSerializer

    def get_queryset(self):
        qs = List.objects.all()
        if not self.request.user.is_staff:
            qs = qs.filter(person=self.request.user)
        return qs

    def perform_create(self, serializer):
        serializer.save(person=self.request.user)
