from django.shortcuts import render,redirect
from django.contrib.auth.models import User

from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .forms import UsersRegisterForm,UsersLoginForm
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.

@login_required
def index(request):
    return render(request,'job_list.html')

def user_login(request):
   
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request,username=username,password= password)
        if user is not None:
            login(request,username)
            return render(request,'job_list.html')
        else:
            messages.info(request,"Username or password is incorrect")
                        
    context = {}
    return render(request,'login.html',context)

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
    return render(request,'sign_up.html',context)

def logout_view(request):
    logout(request)
    return redirect("login")

	# return HttpResponseRedirect("/")
    

def register_view(request):
	form = UsersRegisterForm(request.POST or None)
	if form.is_valid():
		user = form.save()
		password = form.cleaned_data.get("password")	
		user.set_password(password)
		user.save()
		new_user = authenticate(username = user.username, password = password)
		login(request, new_user)
		return redirect("login")
	return render(request, "login_form.html", {
		"title" : "Register",
		"form" : form,
	})

def login_view(request):
	form = UsersLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username = username, password = password)
		login(request, user)
		return redirect("index")
	return render(request, "login_form.html", {
		"form" : form,
		"title" : "Login",
	})