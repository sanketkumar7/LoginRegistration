from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import IntegrityError
from .forms import Student_Registration
from .forms import Student_Update_Form

from .filters import StudentFilters

from django.contrib import messages
import os

from django.views.generic import UpdateView,ListView,DetailView

from .models import Student
# Create your views here.

def check_session(function):
    def wrapper(request, *args, **kwargs):
        if 'UserIsActive' not in request.session:
            return redirect('login') # redirect to the login page if user is not logged in
        return function(request, *args, **kwargs)
    return wrapper

@check_session
def std_registration_view(request,username):
    form=Student_Registration
    if request.method=="POST":
        form=Student_Registration(request.POST, request.FILES)
        if form.is_valid():
                form.save()
                name=form.cleaned_data['full_name']
                messages.success(request,"Record is added for "+name)
                form=Student_Registration
                return render(request,'std_registration/registration.html',{"username":username,'form':form})
    return render(request,'std_registration/registration.html',{"username":username,'form':form})

@check_session
def display_view(request):
    student=Student.objects.all()
    myFilter=StudentFilters(request.GET,queryset=student)
    student=myFilter.qs
    return render(request,'std_registration/display.html',{'student':student,'myFilter':myFilter})

@check_session
def update_view(request,pk):
    student=Student.objects.get(pk=pk)
    #form=Student_Update_Form(mymodel_instance=student)
    form=Student_Update_Form(instance=student)
    if request.method=='POST':
        old_image_path=student.image.path          #saving old_image path
        form=Student_Update_Form(request.POST,request.FILES,instance=student)
        if form.is_valid():      
            form.save(commit=True)                 #updating the students data
            new_image_path=student.image.path      #saving updated students image path
            if old_image_path!=new_image_path:     #checking whether both path aren't pointing to the same.
                os.remove(old_image_path)          #removing old image from the media folder
            return redirect('/display')
    return render(request,'std_registration/update.html',{'form':form})

@check_session
def delete_view(request,pk):
        student=Student.objects.get(pk=pk)
        img_path=student.image.path                 #saving absolute path of image.
        student.delete()
        os.remove(img_path)                        # Removing an image from the media folder.
        return redirect('/display')

class student_list_view(ListView):
     model=Student
     template_name='std_registration/display.html'
     context_object_name='student'
class student_detail_view(DetailView):
     model=Student
     template_name='std_registration/student_detail.html'


    
        
        
        