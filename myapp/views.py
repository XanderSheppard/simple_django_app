from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def index (request):

    data = {
    "Name" : "Xander Sheppard",

    "Track" : "Backend(Python)",

    "Message" : "Hi, Xander, you're doing a great job"
}
    return JsonResponse(data)