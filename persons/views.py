from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Person
from .permissions import SelfOrAdminPersonPermission
from .serializers import PersonSelfSerializer, PersonCreateSerializer
from lists.models import List


class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSelfSerializer
    queryset = Person.objects.all()
    permission_classes = (SelfOrAdminPersonPermission, )

    def get_serializer_class(self):
        if self.action == 'create':
            return PersonCreateSerializer
        return PersonSelfSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        List.objects.create(name='General', person=Person.objects.filter(username=serializer.data.get('username')).first())
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
