from rest_framework.serializers import ModelSerializer, SerializerMethodField
from django.contrib.auth.models import User
from .models import Task

from rest_framework.authtoken.models import Token

class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
