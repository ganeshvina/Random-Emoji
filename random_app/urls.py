from django.contrib import admin
from django.urls import path
from  random_app import views

urlpatterns = [
    path("",views.initial,name="initial"),
    path("home",views.home,name="home"),
    path("searchs",views.searchs,name="searchs"),
]