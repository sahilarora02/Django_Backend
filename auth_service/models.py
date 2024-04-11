from django.db import models

# Create your models here.

class User(models.Model):
    userName = models.CharField(max_length=10)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=20)
    registered_at=models.DateTimeField(auto_now_add=True)
