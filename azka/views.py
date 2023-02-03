from django.shortcuts import render,HttpResponse
from .models import Project,Event,Testimonial,Gallery,Regisration
from django.shortcuts import render,redirect,HttpResponseRedirect,get_object_or_404
from django.contrib import messages
from .forms import ContactForm
from django.db.models import Q
from django.contrib.auth.forms import  AuthenticationForm,PasswordChangeForm,UserChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.forms import  PasswordChangeForm,UserChangeForm
from .forms import signupForm,loginform, updateForm,ProfileForm,testimonialForm
import os
import pathlib


def home(request):
    project=Project.objects.all().order_by('-date')[:12]
    event=Event.objects.all().order_by('-date')[:3]
    gallery=Gallery.objects.all().order_by('-date')[:12]
    testimonial=Testimonial.objects.all().order_by('-date')[:12]
    return render(request,'azka/static_view/home.html',{'events':event,'projects':project,'testimonials':testimonial,'gallery':gallery})


def about(request):
    name="About Us"
    return render(request,'azka/static_view/about.html',{'name':name})


def static_student(request):
    name='Students'
    users=Regisration.objects.all().filter(is_active=True)
    return render(request,'azka/students/static_student.html',{'user':users,'name':name})

    query=request.GET['query']
    value=request.GET['radio_value']
    if value=='department':
        student=Regisration.objects.all().filter(department__icontains=query)
        return render(request,'user/student/search.html',{'student':student,'name':name,'query':query})

    else:
        student=Regisration.objects.all().filter(Passing_Year__icontains=query)
        return render(request,'user/student/search.html',{'student':student,'name':name,'query':query})    


def event(request):
    name="Events"
    event=Event.objects.all().order_by('-date')
    return render(request,'azka/events/event.html',{'events':event,'name':name})


def eventdetail(request,id):
    name="Event"
    event=Event.objects.get(pk=id)
    return render(request,'azka/events/event_detail.html',{'events':event,'name':name}) 


def project(request):
    name="Projects"
    project=Project.objects.all().order_by('-date')
    return render(request,'azka/projects/project.html',{'projects':project,'name':name})


def projectdetail(request,id):
    name="Project"
    project=Project.objects.get(pk=id)
    return render(request,'azka/projects/project_detail.html',{'project':project,'name':name})    


def gallery(request):
    name="Gallery"
    gallery=Gallery.objects.all().order_by('-date')
    return render(request,'azka/gallery/gallery.html',{'name':name,'gallery':gallery}) 


def testimonial(request):
    testimonial=Testimonial.objects.all().order_by('-date')
    return render(request,'azka/testimonial/testimonial.html',{'testimonials':testimonial})


def add_testimonial(request):
    name="Add testimonial" 
    if request.method == 'POST':
        form  = testimonialForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'your testimonial Created Successfuly')
            form.save()
            return redirect(home)
    else:
        form = testimonialForm()
    return render(request, 'azka/testimonial/add_testimonial.html',{'form':form,'name':name})  


def  sign_up(request):
    name="Registration"
    if request.method == 'POST':
        fm=signupForm(request.POST,request.FILES)
        if fm.is_valid():
            user = Regisration.objects.all().filter(username=request.POST.get('username', 'off'))
            if user:
                messages.error(request,'User name already taken')
            else:    
                fm.save()
                messages.success(request,'User successfully added!!wait for profile approvement')
                return redirect(log_in)
    else:
        fm=signupForm()
    return render(request,'user/signup.html',{'form':fm,'name':name}) 


def log_in(request):
    name='Login'
    if request.method == "POST":
        fm=loginform(request.POST)
        if fm.is_valid():
            user = Regisration.objects.filter(username=request.POST.get('username', 'off'), password=request.POST.get('password', 'off'))
            if user:
                user = Regisration.objects.get(username = request.POST.get('username'))    
                if user.is_active == True:
                    request.session['user'] = True
                    request.session['id'] = user.id
                    return redirect('/',user.id)
                else:
                    messages.info(request,'Your Profile Not Approved ')
                    return redirect(log_in)
            else:
                messages.error(request, 'User Name or Password is Incorrect...!')
                return redirect(log_in)
        else:
            return HttpResponse("Invalid Form")       
    else:
        fm=loginform()
        return render(request,'user/login.html',{'form':fm,'name':name}) 



def profile(request,myid):
    name="Profile"
    if request.session.get('user') == True:
        if request.method == 'POST':
            user = Regisration.objects.get(pk=myid)
            form = ProfileForm(request.POST,request.FILES, instance=user)
            image = request.POST.get('image')
            if form.is_valid():
                form.save()
                messages.success(request,'your Data updated successfuly')
                return redirect(profile, myid)
            else:
                return HttpResponse('profile not updated')    
        else:
             user = Regisration.objects.get(pk=myid)
             form = ProfileForm(instance=user)
        return render(request,'user/profile.html',{'form':form,'user':user,'name':name})
    else:
        return redirect(log_in)
  


def edit(request,myid):
    name='Update Profile'
    if request.session.get('user') == True:    
        if request.method == 'POST':
            user = Regisration.objects.get(pk=myid)
            old_image = ""
            if user:
                #old_image = user.image.path
                old_image = pathlib.PureWindowsPath(user.image.path)
                old_image = str(old_image.as_posix())
            form = updateForm(request.POST,request.FILES, instance=user)
            if form.is_valid():
                if os.path.exists(old_image):
                    os.remove(old_image)
                form.save()
                messages.success(request,'your Data updated successfuly')
                return redirect(profile, myid)
            else:
                return HttpResponse('profile not updated')    
        else:
             post = Regisration.objects.get(pk=myid)
             form = updateForm(instance=post)
             return render(request,'edit.html',{'form':form,'post':post,'name':name})


def log_out(request):
    logout(request)
    return redirect(home)


def student(request):
    name="Students"
    if request.session.get('user') == True:
        users=Regisration.objects.all().filter(is_active=True)
        return render(request,'user/student/student.html',{'user':users,'name':name})
    else:
        return redirect(log_in)


def student_detail(request,id):
    name="Student Detail"
    if request.session.get('user') == True:
        users=Regisration.objects.get(pk=id)
    else:
        return redirect(log_in)    
    return render(request,'user/student/student_detail.html',{'user':users,'name':name})    


def search_results(request):
    name="Search Results"
    if request.session.get('user') == True:
        query=request.GET['query']
        value=request.GET['radio_value']
        if value=='department':
            student=Regisration.objects.all().filter(department__icontains=query)
            return render(request,'user/student/search.html',{'student':student,'name':name,'query':query})

        else:
            student=Regisration.objects.all().filter(Passing_Year__icontains=query)
            return render(request,'user/student/search.html',{'student':student,'name':name,'query':query})    

        # query=query.upper()
        # student=Regisration.objects.all().filter(department__icontains=query)
        # student=Regisration.objects.filter(Q(Passing_Year=query)| Q(department=query))     
        return render(request,'user/student/search.html',{'student':student,'name':name,'query':query})
    else:
        return redirect(log_in)               


def contact(request):
    name='Contact'
    form = ContactForm()
    return render(request, "azka/static_view/contact.html", {'form':form,'name':name})
	