from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.paginator import Paginator

def homePage(request):
    
    return render(request, "homePage.html")

def plants(request):

    return render(request, "plants.html")