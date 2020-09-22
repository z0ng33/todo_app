from rest_framework import serializers

from .models import TasksList, Task


class TaskSerializer(serializers.ModelSerializer):
    tasks_list = serializers.PrimaryKeyRelatedField(queryset=TasksList.objects.all(), write_only=True)

    class Meta:
        model = Task
        fields = (
            'id',
            'text',
            'completed',
            'tasks_list',
        )
        read_only_fields = (
            'id',
        )


class TasksListSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = TasksList
        fields = (
            'id',
            'name',
            'tasks',
        )
        read_only_fields = (
            'id',
            'tasks',
        )
