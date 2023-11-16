from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Task


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = ["last_modified", "created"]

    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), required=False
    )
