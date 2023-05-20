from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def chinnu(request):
    return HttpResponse('<h1>This is chinmayi</h1>')
def manu(request):
    return HttpResponse('<marquee>This is manu</marquee>')
