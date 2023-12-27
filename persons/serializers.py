from rest_framework import serializers
from .models import Person


class PersonCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ('username', 'first_name', 'last_name', 'email', 'birthday', 'password')

    def create(self, validated_data):
        person = Person.objects.create_user(**validated_data)
        return person


class PersonSelfSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ('username', 'first_name', 'last_name', 'email', 'birthday')
