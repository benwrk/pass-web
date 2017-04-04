from django.db import models

# Create your models here.
class Message(models.Model):
    mac = models.CharField(max_length=12)
    message = models.TextField()