from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
  return HttpResponse('<h1>This is home page</h1>')

def greet2(request):
  return HttpResponse("<h1>This is second page</h1>")