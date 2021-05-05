from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from django.contrib import messages
# Create your views here.

@login_required
def index(request):
    return render(request,'accounts/index.html')

def user_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,username)
            return render(request,'accounts/index.html')
            
    context['form']=form
    return render(request,'registration/login.html',context)

def sign_up(request):
    context = {}
    form = CreateUserForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            name = form.cleaned_data.get('username')
            messages.success(request,"Account was created for "+ name)
            # login(request,user)
            # return render(request,'accounts/index.html')
            redirect("login")
    context['form']=form
    return render(request,'registration/sign_up.html',context)