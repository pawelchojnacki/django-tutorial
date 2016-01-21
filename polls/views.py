from django.shortcuts import render
from django.http import HttpResponse


def indeksik(request):
    return HttpResponse("Hello, world XD")

def aha(request):
	return HttpResponse("OH FUCK IT WORKS")