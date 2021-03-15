from django.db import models
from datetime import datetime


class Todos(models.Model):
    todo = models.TextField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.todo
