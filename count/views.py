from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello,Nepal. Your People count is 2 crore 93 lakh')