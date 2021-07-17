from django.http import HttpResponse, JsonResponse
from server import services, models, serializers
from django.shortcuts import redirect
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return HttpResponse("Hello, world. You're at the vMail index.")


def allMessages(request):
    if request.method == 'GET':
        allMessages = models.MessageModel.objects.all()
        serializer = serializers.MessageSerializer(allMessages, many=True)
        print(serializer.data)
        return HttpResponse()
    else:
        print("erro")


def editMessage(request, messageID):
    services.editMessage()
    response = "Details about %s message"
    return HttpResponse(response % messageID)


def deleteMessage(request):
    services.deleteMessage()
    return HttpResponse()


def getMessage(request, messageID):
    services.getMessage()
    response = 'Details absout a specifc message'
    return HttpResponse()


@csrf_exempt
def registerMessage(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = serializers.MessageSerializer(data=data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return HttpResponse()
        return HttpResponse()
    else:
        print("erro")
        return HttpResponse()
