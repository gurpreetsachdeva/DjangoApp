from django.shortcuts import render
from django.http import HttpResponse
def hi(request):
    return HttpResponse("<h1>This is my home page</h1>")
# Create your views here.
