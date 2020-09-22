from django.db import models


class TasksList(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)


class Task(models.Model):
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    tasks_list = models.ForeignKey(TasksList, null=False, on_delete=models.CASCADE, related_name='tasks')

    class Meta:
        ordering = ('created_at',)
