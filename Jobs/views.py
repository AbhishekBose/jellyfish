from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@login_required
def index(request):
    return HttpResponse("Welcome to the training job page")