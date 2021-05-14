from django import http
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required

from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from .serializers import JobSerializer,CreateJobSerializer,UpdateJobSerializer
from .models import Jobs

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .tasks import celery_task

# Create your views here.
@login_required
def index(request):
    return HttpResponse("Welcome to the training job page")

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def apiOverview(request):
    api_list = {
        "List":"/job-list",
        "Detail View":"task-detail/<str:pk>/",
        "Create":"/task-create/",
        "Update":"/task-update/<str:pk>/",
        "Delete":"/task-delete/<str:pk>/",
    }

    return Response(api_list)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def JobList(request):

    jobs = Jobs.objects.filter(user=request.user)
    serializer = JobSerializer(jobs,many=True)
    return Response(serializer.data)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def JobDetail(request,pk):

    try:
        jobs = Jobs.objects.get(id=pk)
    except Jobs.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = JobSerializer(jobs,many=False)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def JobCreate(request):

    serializer = CreateJobSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(["POST"])
@permission_classes([IsAuthenticated])
def JobUpdate(request,pk):
    try:
        jobs = Jobs.objects.get(id=pk)
    except Jobs.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = UpdateJobSerializer(instance=jobs,data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def JobDelete(request,pk):
    try:
        jobs = Jobs.objects.get(id=pk)
    except Jobs.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    jobs.delete()
    return Response("Item successfully deleted",status=status.HTTP_204_NO_CONTENT)


def JobTest(request):
    celery_task.delay(10)
    return HttpResponse("Done ")