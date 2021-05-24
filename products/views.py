from django.shortcuts import HttpResponse
from django.shortcuts import render


# /products -> index
# uniform resource locator (address)

def index(request):
    return HttpResponse("Hello World")


def new(request):
    return HttpResponse('New Products')
