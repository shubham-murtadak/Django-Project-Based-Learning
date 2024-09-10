from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index2(request):
  return HttpResponse("This is app2 index page!")

def np2(request):
  return HttpResponse("This is app2 np2 function!")

def next_page(request):
  return HttpResponse('<a href="/app1/index">App1</a>')