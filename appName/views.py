from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
# Mail Use Garne
from django.core.mail import send_mail
from django.template.loader import render_to_string
# Password Change
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required


# Create your views here.
date= datetime.now().year

def index(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.PoST['email']
        phone=request.POST['phone']
        messageback=request.POST['message'] 

        subject=""
        message=render_to_string('appName/message.html',{'name':name,'message':messageback})
        from_email=email
        recipient_list="surakshyabalami980@gmail.com"
        request 
        send_mail(subject,message,from_email,recipient_list, fail_silently=False)

        messages.success(request,f"Thank You {name} Your Response was submitted Successfully ")
        return redirect('index')
    
    return render (request,'appName/index.html', {'date':date})

def about(request):
    return render (request,'appName/about.html', {'date':date})
def contact(request):
    return render (request,'appName/contact.html', {'date':date})
def services(request):
    return render (request,'appName/services.html', {'date':date})
def menu(request):
    return render (request,'appName/menu.html', {'date':date})

def register(request):
    if request.method=='POST':
        name=request.POST['name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirmPassword=request.POST['password1']

        if password==confirmPassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Already Exits")
                print("UserNAme already exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Exits ")
                return redirect('register')
            else:
                User.objects.create_user(first_name=name,username=username, email=email, password=password)
                messages.success(request, "Registered Successfully ")
                return redirect("login")
        else:
            messages.error(request, "Password Doesnot Match ")
            return redirect('register')
    return render (request,'auth/register.html' )


def log_in(request):
    if request.method=='POST':

        username=request.POST['username']

        password=request.POST['password']

        if not User.objects.filter(username=username).exists():
            messages.info(request,"User name Does Not Exits ")
            return redirect ('login')
        
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.error(request," Password Mismatch ")
            return redirect('login')

    return render (request, 'auth/login.html')

def log_out(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def change_password(request):
    form=PasswordChangeForm(user=request.user)
    if request.method=='POST':
        form=PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            # form.save()
            name=form.save()
            update_session_auth_hash(request,name)
            return redirect('login')
    return render(request, 'auth/change_password.html',{'form':form})

