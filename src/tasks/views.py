from rest_framework.viewsets import ModelViewSet

from .models import TasksList
from .serializers import TasksListSerializer


class TasksListsViewSet(ModelViewSet):
    queryset = TasksList.objects.all()
    serializer_class = TasksListSerializer
