from django.db import models

class Message(models.Model):
    subject = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)
    startDate = models.DateTimeField()
    expirationDate = models.DateTimeField()
