from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def get_app3(request):
    return HttpResponse('This is app3')
