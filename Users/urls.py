from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from . import views



urlpatterns = [ 
    path('',views.index,name="home"),
    # path('register/',views.sign_up,name="sign-up"),
    # path('login/',views.user_login,name="login"),
    # path('logout/',views.logout_view,name="logout"),
    url(r"^register",views.register_view,name="sign-up"),
    url(r"^login/",views.login_view,name="login"),
    url(r"^logout",views.logout_view,name="logout")
]