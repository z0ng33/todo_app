from rest_framework import serializers

from .models import TasksList


class TasksListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TasksList
        fields = (
            'name',
        )
