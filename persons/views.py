from rest_framework import viewsets
from .models import Person
from .permissions import SelfOrAdminPersonPermission
from .serializers import PersonSelfSerializer, PersonCreateSerializer


class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSelfSerializer
    queryset = Person.objects.all()
    permission_classes = SelfOrAdminPersonPermission

    def get_serializer_class(self):
        if self.action == 'create':
            return PersonCreateSerializer
        return PersonSelfSerializer
