from rest_framework import serializers
from .models import Person


class PersonSelfSerializer(serializers.ModelSerializer):
    birth_date = serializers.DateField(
        format='%d.%m.%Y',
        input_formats=['%d.%m.%Y', ],
    )

    class Meta:
        model = Person
        fields = ('username', 'first_name', 'last_name', 'email', 'birth_date')


class PersonCreateSerializer(PersonSelfSerializer):

    class Meta(PersonSelfSerializer.Meta):
        fields = ('username', 'first_name', 'last_name', 'email', 'birth_date', 'password')

    def create(self, validated_data):
        person = Person.objects.create_user(**validated_data)
        return person


