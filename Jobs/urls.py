from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('',views.index,name="home"),
    path("",views.apiOverview,name="api-overview"),
    path("home",views.index,name="index"),
    path("models",views.ModelView,name="models"),
    path("job-list",views.JobList,name="job-list"),
    path("job-detail/<str:pk>",views.JobDetail,name="job-detail"),
    path("job-create/",views.JobCreate,name="job-create"),
    path("job-update/<str:pk>",views.JobUpdate,name="job-update"),
    path("job-status-update/<str:pk>",views.JobStatusUpdate,name="job-status-update"),
    path("job-trigger/<str:pk>",views.JobTrigger,name="job-trigger"),
    path("job-delete/<str:pk>",views.JobDelete,name="job-delete"),
    path("job-test/",views.JobTest,name="job-test"),
    path("job-detail-page/<str:pk>",views.JobDetailPage,name="job-detail-page"),
    path("job-create-page/",views.JobCreatePage,name="job-create-page"),
    path("job-update-page/<str:pk>",views.JobUpdatePage,name="job-update-page"),
    path("job-delete-page/<str:pk>",views.JobDeletePage,name="job-delete-page"),
    path("job-trigger-action/<str:pk>",views.JobTriggerAction,name="job-trigger-action"),
]   