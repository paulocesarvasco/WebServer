from django.http import HttpResponse
from server import services


def index(request):
    return HttpResponse("Hello, world. You're at the vMail index.")

def allMessages(request):
    services.showMessage()
    return HttpResponse()

def messageDetails(request, messageID):
    response = "Details about %s message"
    return HttpResponse(response % messageID)
