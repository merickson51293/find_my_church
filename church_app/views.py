from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import *

def index(request):
    return render(request, "index.html")

def church_reg_log(request):
    return render(request, "church_reg_log.html")

def create_user(request):
    if request.method=="POST":
        errors=User.objects.validator(request.POST)
        if errors:
            for error in errors:
                messages.error(request, errors[error])
            return redirect('/')
        user_pw=request.POST['password']
        hash_pw=bcrypt.hashpw(user_pw.encode(), bcrypt.gensalt()).decode()
        new_user=User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=hash_pw)
        request.session['user_id']=new_user.id
        request.session['user_name']=f"{new_user.first_name} {new_user.last_name}"
        return redirect("/main")
    return redirect('/')

def login(request):
    if request.method=="POST":
        errors=User.objects.login_validator(request.POST)
        if errors:
            for error in errors:
                messages.error(request, errors[error])
            return redirect('/')
        logged_user=User.objects.filter(email=request.POST['email'])
        if logged_user:
            logged_user=logged_user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['user_id']=logged_user.id
                request.session['user_name']=f"{logged_user.first_name} {logged_user.last_name}"
                return redirect('/main')
    return redirect('/')

def create_church(request):
    if request.method=="POST":
        errors=Church.objects.church_validator(request.POST)
        if errors:
            for error in errors:
                messages.error(request, errors[error])
            return redirect('/church_reg_log')
        church_pw=request.POST['password']
        hash_pw=bcrypt.hashpw(church_pw.encode(), bcrypt.gensalt()).decode()
        new_church=Church.objects.create(church_name=request.POST['church_name'], admin_name=request.POST['admin_name'], admin_email=request.POST['admin_email'], password=hash_pw)
        request.session['church_id']=new_church.id
        request.session['church_name']=f"{new_church.church_name}"
        request.session['admin_name']=f"{new_church.admin_name}"
        request.session['admin_email']=f"{new_church.admin_email}"
        return redirect("/church_info")
    return redirect('/')

def church_login(request):
    if request.method=="POST":
        errors=Church.objects.church_login_validator(request.POST)
        if errors:
            for error in errors:
                messages.error(request, errors[error])
            return redirect('/church_reg_log')
        logged_church=Church.objects.filter(admin_email=request.POST['admin_email'])
        if logged_church:
            logged_church=logged_church[0]
            if bcrypt.checkpw(request.POST['password'].encode(), logged_church.password.encode()):
                request.session['church_id']=logged_church.id
                request.session['church_name']=f"{logged_church.church_name}"
                request.session['admin_name']=f"{logged_church.admin_name}"
                request.session['admin_email']=f"{logged_church.admin_email}"
                return redirect('/church_main')
    return redirect('/')

def church_info(request):
    return render(request, "church_info.html")

def church_contact(request):
    return render(request, "church_contact.html")

def church_beliefs(request):
    return render(request, "church_beliefs.html")

def church_pastor(request):
    return render(request, "church_pastor.html")

def church_info_other(request):
    return render(request, "church_info_other.html")

def church_success(request):
    return render(request, "church_success.html")

def church_main(request):
    return render(request, "church_main.html")

def church_profile(request):
    return render(request, "church_profile.html")

def church_logout(request):
    request.session.clear()
    return redirect('/church_reg_log')

def test(request):
    return render(request, "test.html")