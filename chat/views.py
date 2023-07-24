import json
from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import HttpResponse, render, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    return HttpResponse("working")