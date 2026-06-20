from django.db import models
from django.contrib.auth.models import User


class notes(models.Model):
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.title