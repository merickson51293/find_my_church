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

def church_success(request):
    
    return render(request, "church_success.html")

def create_church(request):
    if request.method=="POST":
        errors=Church.objects.church_validator(request.POST)
        if errors:
            for error in errors:
                messages.error(request, errors[error])
            return redirect('/church_reg_log')
        church_pw=request.POST['password']
        hash_pw=bcrypt.hashpw(church_pw.encode(), bcrypt.gensalt()).decode()
        request.session['church_name']=f"{request.POST['church_name']}"
        request.session['admin_name']=f"{request.POST['admin_name']}"
        request.session['admin_email']=f"{request.POST['admin_email']}"
        request.session['password']=hash_pw
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

def create_church_contact(request):
    if request.method=="POST":
        request.session['city_state']=f"{request.POST['city_state']}"
        request.session['address']=f"{request.POST['address']}"
        request.session['website']=f"{request.POST['website']}"
        request.session['facebook']=f"{request.POST['facebook']}"
        request.session['instagram']=f"{request.POST['instagram']}"
        request.session['twitter']=f"{request.POST['twitter']}"
        request.session['church_email']=f"{request.POST['church_email']}"
        request.session['church_phone']=f"{request.POST['church_phone']}"
        return redirect('/church_beliefs')

def church_beliefs(request):
    return render(request, "church_beliefs.html")

def create_church_beliefs(request):
    if request.method=="POST":
        request.session['denomination']=f"{request.POST['denomination']}"
        request.session['values']=f"{request.POST['values']}"
        request.session['size']=f"{request.POST['size']}"
        request.session['youngest']=f"{request.POST['youngest']}"
        request.session['younger']=f"{request.POST['younger']}"
        request.session['young']=f"{request.POST['young']}"
        request.session['old']=f"{request.POST['old']}"
        request.session['oldest']=f"{request.POST['oldest']}"
        return redirect('/church_info_other')

def church_info_other(request):
    return render(request, "church_info_other.html")

def create_church_info_other(request):
    new_church=Church.objects.create(church_name=request.session['church_name'], admin_name=request.session['admin_name'], admin_email=request.session['admin_email'], password=request.session['password'], city_state=request.session['city_state'], address=request.session['address'],website=request.session['website'],facebook=request.session['facebook'], instagram=request.session['instagram'], twitter=request.session['twitter'], church_email=request.session['church_email'], church_phone=request.session['church_phone'], denomination=request.session['denomination'], values=request.session['values'], size=request.session['size'], youngest=request.session['youngest'], younger=request.session['younger'], young=request.session['young'], old=request.session['old'], oldest=request.session['oldest'], other=request.POST['other'])
    return redirect('/church_pastor')

def create_pastor(request):
    if request.method=='POST':
        new_pastor= Pastor.objects.create(pastor_name=request.POST['pastor_name'], pastor_title=request.POST['pastor_title'], pastor_email=request.POST['pastor_email'], pastor_phone=request.POST['pastor_phone'], pastor_social=request.POST['pastor_social'])
        return redirect('/church_pastor')

def church_pastor(request):
    context={
        'all_pastors': Pastor.objects.all()
    }
    return render(request, "church_pastor.html", context)

def church_main(request):
    context={
       'all_churches': Church.objects.all() 
    }
    return render(request, "church_main.html", context)

def church_profile(request, church_id):
    context={
        'one_church': Church.objects.get(id=church_id)
    }
    return render(request, "church_profile.html", context)

def logout(request):
    request.session.clear()
    return redirect('/church_reg_log')

def add_message(request):
    message = Message.objects.create(message=request.POST['message'], church=Church.objects.get(id=request.session['church_id']))
    return redirect('/home_page')

def delete(request, message_id):
    message=Message.objects.get(id=message_id)
    message.delete()
    return redirect('/home_page')

def delete_church(request, church_id):
    church=Church.objects.get(id=church_id)
    church.delete()
    return redirect('/home_page')

def home_page(request):
    context={
        'all_churches': Church.objects.all(),
        'all_messages': Message.objects.all(),
    }
    return render(request, "home_page.html", context)

