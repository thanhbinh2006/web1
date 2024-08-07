from django.contrib import admin
from django.urls import path
from . import views 
urlpatterns = [
    path('',views.get_app1),
    path('child1',views.get_child1_app1),
    path('child2',views.get_child2_app1)
]
