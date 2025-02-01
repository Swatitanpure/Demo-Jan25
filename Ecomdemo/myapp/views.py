from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(Requests):

    return HttpResponse("Hello Django, This is my 1st Project")

