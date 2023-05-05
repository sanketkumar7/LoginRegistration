from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import loginForm
from .forms import SignupForm
from .models import admin
# Create your views here.
def welcome_view(request):
    if 'UserIsActive' in request.session:
        return redirect('stdregistration',username=request.session['UserIsActive'])
    return render(request,'login/welcome.html')
def login_view(request):
    form=loginForm
    if request.method=='POST':
       form=loginForm(request.POST)
       if form.is_valid():
           username=form.cleaned_data.get('username')
           password=form.cleaned_data.get('password')
           if admin.objects.filter(username=username,password=password).exists():
               request.session['UserIsActive']=username
               return redirect('stdregistration',username=username)
    return render(request,'login/login.html',{'form':form})
def signup_view(request):
    form=SignupForm
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            first_name=form.cleaned_data.get('first_name')
            last_name=form.cleaned_data.get('last_name')
            email=form.cleaned_data.get('email')
            password=form.cleaned_data.get('password')
            new_user=admin(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
            new_user.save()
            return render(request,'login/welcome.html',{'msg':"User "+username+" added."})
    return render(request,'login/signup.html',{'form':form})
def logout_key_view(request):
    if 'UserIsActive' in request.session: 
        del request.session['UserIsActive']
    return redirect('login')
def about_us_view(request):
    return render(request,'login/aboutus.html')
