from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('',views.index,name="home"),
    path("",views.apiOverview,name="api-overview"),
    path("job-list",views.JobList,name="job-list"),
    path("job-detail/<str:pk>",views.JobDetail,name="job-detail"),
    path("job-create/",views.JobCreate,name="job-create"),
    path("job-update/<str:pk>",views.JobUpdate,name="job-update"),
    path("job-status-update/<str:pk>",views.JobStatusUpdate,name="job-status-update"),
    path("job-delete/<str:pk>",views.JobDelete,name="job-delete"),
    path("job-test/",views.JobTest,name="job-test"),
    
]   