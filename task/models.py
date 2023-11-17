from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    class Meta:
        ordering = ["-created"]

    class TaskStatusChoices(models.TextChoices):
        TO_DO = "TO_DO", "TO_DO"
        IN_PROGRESS = "IN_PROGRESS", "IN_PROGRESS"
        DONE = "DONE", "DONE"

    class TaskPriorityChoices(models.TextChoices):
        LOW = "Low", "Low"
        MEDIUM = "Medium", "Medium"
        HIGH = "High", "High"

    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(
        null=True, blank=True, help_text="Give some info about the task"
    )
    status = models.CharField(
        max_length=25,
        choices=TaskStatusChoices.choices,
        default=TaskStatusChoices.TO_DO,
    )

    priority = models.CharField(
        max_length=25,
        choices=TaskPriorityChoices.choices,
        default=TaskPriorityChoices.LOW,
    )

    due_date = models.DateTimeField(blank=True, null=True)

    last_modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
