from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="home"),
    path('register/',views.sign_up,name="sign-up"),
    path('login/',views.user_login,name="login")
]