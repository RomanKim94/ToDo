from rest_framework import serializers

from .models import Task


class TaskListSerializer(serializers.ModelSerializer):
    deadline = serializers.DateTimeField(
        format='%d.%m.%Y %H:%M',
        input_formats=['%d.%m.%Y %H:%M', ],
    )

    class Meta:
        model = Task
        fields = ('name', 'is_done', 'deadline', 'list')


class TaskDetailSerializer(TaskListSerializer):

    class Meta(TaskListSerializer.Meta):
        fields = '__all__'
