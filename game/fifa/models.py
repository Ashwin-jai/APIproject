from django.db import models
from uuid import uuid4
class Employee(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, unique=True)
    name = models.CharField(max_length=225)
    email = models.CharField(max_length=225)
    job = models.CharField(max_length=225)


    def __str__(self):
        return self.name

# Create your models here.
