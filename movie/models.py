from pydoc import describe
from django.db import models
from django.contrib.auth.models import AbstractUser, User


class Task(models.Model):
    content = models.CharField(max_length=255)

    def __str__(self):
        return '%s' % (self.content)
