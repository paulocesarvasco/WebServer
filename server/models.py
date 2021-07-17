from django.db import models


class MessageModel(models.Model):
    subject = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)
    startDate = models.DateTimeField(auto_now_add=True)
    expirationDate = models.DateTimeField(auto_now_add=True)

    def getSubject(self):
        return self.subject
