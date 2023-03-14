from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def showw(request):
    return HttpResponse('Lets Authenticat3')

def calcr(request):
    C=9+10
    return HttpResponse(C)
