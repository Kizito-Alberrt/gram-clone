from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class post(models.Model):
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
