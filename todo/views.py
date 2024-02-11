from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("This is the index page")


def register(request):
    return HttpResponse("This is the register page")


def login(request):
    return HttpResponse("This is the Login page")


def create_task(request):
    return HttpResponse("This is the create page")


def update_task(request):
    return HttpResponse("This is the update page")


def delete_task(request):
    return HttpResponse("This is the delete page")
