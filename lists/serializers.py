from rest_framework import serializers

from .models import List
from tasks.serializers import TaskListSerializer


class ListListSerializer(serializers.ModelSerializer):

    class Meta:
        model = List
        fields = ('name',)


class ListDetailSerializer(ListListSerializer):
    Tasks = TaskListSerializer(many=True)

    class Meta(ListListSerializer.Meta):
        fields = ('name', 'Tasks')
