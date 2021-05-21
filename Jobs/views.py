from django import http
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required

from rest_framework.decorators import api_view,permission_classes
from rest_framework.renderers import JSONRenderer

from rest_framework.response import Response
from .serializers import JobSerializer,CreateJobSerializer,UpdateJobSerializer,UpdateJobStatusSerializer,TriggerJobSerializer
from .models import Jobs
from .trigger import Trigger
from .forms import JobForm
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .tasks import celery_task

# Create your views here.
@login_required
def index(request):
    # return HttpResponse("Welcome to the training job page")
    jobs = Jobs.objects.filter(user=request.user)
    print(jobs)
    context = {
        "objects": jobs
    }
    return render(request,"job_list.html",context)

@login_required
def ModelView(request):
    # return HttpResponse("Welcome to the training job page")
    models = {
        "modelName":"YOLO",
        "modelTypes":["detector","classification","segmentation"]
    }
    return render(request,"models.html",models)



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
    renderer_classes = [JSONRenderer]
    jobs = Jobs.objects.filter(user=request.user)
    serializer = JobSerializer(jobs,many=True)
    # return Response(serializer.data)
    print(serializer.data)
    return Response(serializer.data)
    # return Response(serializer.data,"")


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def JobDetail(request,pk):
    
    try:
        jobs = Jobs.objects.get(id=pk)
    except Jobs.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = JobSerializer(jobs,many=False)
    return Response(serializer.data)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def JobDetailPage(request,pk):
    
    try:
        jobs = Jobs.objects.get(id=pk)
    except Jobs.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    context = {
        "object":jobs
    }
    # serializer = JobSerializer(jobs,many=False)
    # return Response(serializer.data)
    return render(request,"job_detail.html",context)



@api_view(["POST"])
@permission_classes([IsAuthenticated])
def JobCreate(request):

    serializer = CreateJobSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(["POST"])
@permission_classes([IsAuthenticated])
def JobCreatePage(request):
    form = JobForm(request.POST or None)
    if form.is_valid():
        model =  form.save(commit=False)
        model.user = request.user
        model.save()
        form = JobForm()
        return redirect("index")
    else:
        print("Form is not valid")
    
    context = {
        "form":form
    }
    return render(request,"job_create.html",context)
    # serializer = CreateJobSerializer(data=request.data)
    # if serializer.is_valid():
    #     serializer.save(user=request.user)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUES

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

# @api_view(["POST"])
@permission_classes([IsAuthenticated])
def JobUpdatePage(request,pk):
    try:
        jobs = Jobs.objects.get(id=pk)
        form = JobForm(instance=jobs)

        if request.method == "POST":
            form = JobForm(request.POST,instance=jobs)
            if form.is_valid():
                model =  form.save(commit=False)
                model.user = request.user
                model.save()
            return redirect("index")
                # form = JobForm(instance=jobs)
        context ={
            "form":form
        }
    except Jobs.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return render(request,"job_update.html",context)
    # serializer = UpdateJobSerializer(instance=jobs,data=request.data)
    # if serializer.is_valid():
    #     serializer.save(user=request.user)
    #     return Response(serializer.data)
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@permission_classes([IsAuthenticated])
def JobDeletePage(request,pk):
    try:
        jobs = Jobs.objects.get(id=pk)
        if request.method == "POST":
            jobs.delete()
            return redirect("index")
        context ={
            "item":jobs
        }
    except Jobs.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return render(request,"job_delete.html",context)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def JobInitiate(request,pk):
    try:
        jobs = Jobs.objects.get(id=pk)
    except Jobs.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = UpdateJobSerializer(instance=jobs,data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(["POST"])
# @permission_classes([IsAuthenticated])
def JobStatusUpdate(request,pk):
    try:
        jobs = Jobs.objects.get(id=pk)
    except Jobs.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = UpdateJobStatusSerializer(instance=jobs,data=request.data)
    if serializer.is_valid():
        # serializer.save(user=request.user)
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def JobTrigger(request,pk):
    try:
        jobs = Jobs.objects.get(id=pk)
        print(jobs)
    except Jobs.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    if jobs.user != request.user:
        return Response(request.data, status=status.HTTP_403_FORBIDDEN)
    else:
        data = {
            "id":pk,
            "job_status":"INIT"
        }
        serializer = TriggerJobSerializer(instance=jobs,data=data)
        if serializer.is_valid():
            print("Serializer is valid")
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