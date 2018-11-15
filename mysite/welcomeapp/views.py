from django.shortcuts import render
from django.http import HttpResponse
def welcome(request):
    return HttpResponse("<html><head></head><body bgcolor=pink><center>welcome to the djangoproject</center></body></html>")

