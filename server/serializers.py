from rest_framework import serializers
from server import models


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MessageModel
        fields = '__all__'

    def create(self, data):
        return models.MessageModel.objects.create(**data)

    def update(self, instance, data):
        instance.subject = data.get('subject', instance.subject)
        instance.content = data.get('content', instance.content)
        instance.startDate = data.get('startDate', instance.startDate)
        instance.expirationDate = data.get('expirationDate', instance.expirationDate)
        instance.save()
        return instance
