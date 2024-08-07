from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def get_app1(request):
    return render(request,'app1.html')
def get_child1_app1(request):
    return HttpResponse('This is child 1 of app1')
def get_child2_app1(requset):
    return HttpResponse('This is child 2 of app1')