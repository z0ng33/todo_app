from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins

from .models import TasksList, Task
from .serializers import TaskSerializer, TasksListSerializer


class TasksListsViewSet(ModelViewSet):
    queryset = TasksList.objects.prefetch_related('tasks').all()
    serializer_class = TasksListSerializer


class TasksViewSet(mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   GenericViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
