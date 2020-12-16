from django.http import HttpResponse 
from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import *
from .forms import *
from .utils import *

def index(request):
    return render(request, "index.html")

def guest(request):
    return render(request, "guest.html")

def user_reg(request):
    return render(request, "user_reg/user_reg.html")

def church_reg_log(request):
    return render(request, "church_reg/church_reg_log.html")

def create_user(request):
    if request.method=="POST":
        errors=User.objects.validator(request.POST)
        if errors:
            for error in errors:
                messages.error(request, errors[error])
            return redirect('/')
        user_pw=request.POST['password']
        hash_pw=bcrypt.hashpw(user_pw.encode(), bcrypt.gensalt()).decode()
        # new_user=User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=hash_pw)
        # request.session['user_id']=new_user.id
        request.session['first_name']=request.POST['first_name']
        request.session['last_name']=request.POST['last_name']
        request.session['email']=request.POST['email']
        request.session['password']=hash_pw
        return redirect("/user_info")
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
                return redirect('/user_home_page')
    return redirect('/')

def church_success(request):
    return render(request, "church/church_success.html")

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
        logged_churches=Church.objects.filter(admin_email=request.POST['admin_email'])
        if logged_churches:
            logged_church=logged_churches[0]
            if bcrypt.checkpw(request.POST['password'].encode(), logged_church.password.encode()):
                request.session['church_id']=logged_church.id
                print(f"Church ID is set {logged_church.id}")
                request.session['church_name']=f"{logged_church.church_name}"
                request.session['admin_name']=f"{logged_church.admin_name}"
                request.session['admin_email']=f"{logged_church.admin_email}"
                return redirect('/church_home_page')
    return redirect('/')

def user_info(request):
    return render(request, "user_reg/user_info.html")

def user_contact(request):
    return render(request, "user_reg/user_contact.html")

def create_user_contact(request):
    if request.method=="POST":
        request.session['user_city']=f"{request.POST['user_city']}"
        request.session['user_state']=f"{request.POST['user_state']}"
        request.session['user_address']=f"{request.POST['user_address']}"
        request.session['user_email']=f"{request.POST['user_email']}"
        request.session['user_facebook']=f"{request.POST['user_facebook']}"
        request.session['user_instagram']=f"{request.POST['user_instagram']}"
        request.session['adults']=f"{request.POST['adults']}"
        request.session['teens']=f"{request.POST['teens']}"
        request.session['kids']=f"{request.POST['kids']}"
        request.session['user_phone']=f"{request.POST['user_phone']}"
        return redirect('/user_church')

def user_church(request):
    return render(request, "user_reg/user_church.html")

def create_user_church(request):
    if request.method=="POST":
        request.session['denomination']=f"{request.POST['denomination']}"
        request.session['church_size']=f"{request.POST['church_size']}"
        request.session['student_programs']=f"{request.POST['student_programs']}"
        request.session['small_groups']=f"{request.POST['small_groups']}"
        return redirect('/user_info_other')

def user_info_other(request):
    return render(request, "user_reg/user_info_other.html")

def finish_user(request):
    new_user=User.objects.create(first_name=request.session['first_name'], last_name=request.session['last_name'], email=request.session['user_email'], password=request.session['password'], user_address=request.session['user_address'],user_city=request.session['user_city'],user_state=request.session['user_state'], user_email=request.session['user_email'], user_facebook=request.session['user_facebook'], user_instagram=request.session['user_instagram'], adults=request.session['adults'], teens=request.session['teens'], kids=request.session['kids'], user_phone=request.session['user_phone'], denomination=request.session['denomination'], church_size=request.session['church_size'], student_programs=request.session['student_programs'], small_groups=request.session['small_groups'], user_info_other=request.POST['user_info_other'])
    request.session['user_id']=new_user.id
    return redirect("/user_pic")

def user_pic(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        print("being to process post request")
        if form.is_valid():
            print("post data was valid")
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'home_page.html', {'form': form, 'img_obj': img_obj})
    form=ImageForm()
    return render(request, "user_reg/user_pic.html", {'form' : form})

def church_info(request):
    return render(request, "church_reg/church_info.html")

def church_contact(request):
    return render(request, "church_reg/church_contact.html")

def create_church_contact(request):
    if request.method=="POST":
        request.session['church_city']=f"{request.POST['church_city']}"
        request.session['church_state']=f"{request.POST['church_state']}"
        request.session['address']=f"{request.POST['address']}"
        request.session['website']=f"{request.POST['website']}"
        request.session['facebook']=f"{request.POST['facebook']}"
        request.session['instagram']=f"{request.POST['instagram']}"
        request.session['church_email']=f"{request.POST['church_email']}"
        request.session['church_phone']=f"{request.POST['church_phone']}"
        return redirect('/church_beliefs')

def church_beliefs(request):
    return render(request, "church_reg/church_beliefs.html")

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
    return render(request, "church_reg/church_info_other.html")

def create_church_info_other(request):
    new_church=Church.objects.create(church_name=request.session['church_name'], admin_name=request.session['admin_name'], admin_email=request.session['admin_email'], password=request.session['password'], church_city=request.session['church_city'], church_state=request.session['church_state'], address=request.session['address'],website=request.session['website'],facebook=request.session['facebook'], instagram=request.session['instagram'], church_email=request.session['church_email'], church_phone=request.session['church_phone'], denomination=request.session['denomination'], values=request.session['values'], size=request.session['size'], youngest=request.session['youngest'], younger=request.session['younger'], young=request.session['young'], old=request.session['old'], oldest=request.session['oldest'], other=request.POST['other'])
    request.session['church_id']=new_church.id
    return redirect('/church_pastor')

def create_pastor(request):
    if request.method=='POST':
        new_pastor= Pastor.objects.create(pastor_name=request.POST['pastor_name'], pastor_title=request.POST['pastor_title'], pastor_email=request.POST['pastor_email'], pastor_phone=request.POST['pastor_phone'], pastor_social=request.POST['pastor_social'])
        new_pastor.church.add(Church.objects.get(id=request.session['church_id']))
        return redirect('/church_pastor')

def church_pastor(request):
    church=Church.objects.get(id=request.session['church_id'])
    context={
        'church_pastors': church.church_pastor.all()
    }
    return render(request, "church_reg/church_pastor.html", context)

def logout(request):
    request.session.clear()
    return redirect('/')

def add_message(request):
    user=User.objects.get(id=request.session['user_id'])
    message = UserMessage.objects.create(message=request.POST['message'], user=user)
    return redirect('/user_home_page')

def church_profile(request, church_id):
    churchobj=Church.objects.get(id=church_id)
    if isloggedinuser(request.session):
        user_id=request.session.get("user_id", "invalid")
        userobj=User.objects.get(id=user_id)
        dm = DirectMessages.objects.filter(user=userobj, church=churchobj)
    else:
        dm = DirectMessages.objects.filter(church=churchobj)
    context={
        'one_church': churchobj,
        'dm': dm
    }
    return render(request, "church/church_profile.html", context)

def user_profile(request, user_id):
    userobj=User.objects.get(id=user_id)
    if isloggedinchurch(request.session):
        church_id=request.session.get("church_id", "invalid")
        churchobj=Church.objects.get(id=church_id)
        dm = DirectMessages.objects.filter(user=userobj, church=churchobj)
    else:
        dm = DirectMessages.objects.filter(user=userobj)
    context={
        'one_user': userobj,
        'dm': dm
    }
    return render(request, "user/user_profile.html", context)

def add_direct_message(request):
    user=User.objects.get(id=request.POST['user_id'])
    church=Church.objects.get(id=request.POST['church_id'])
    dm = DirectMessages.objects.create(dm=request.POST['dm'], user=user, church=church)
    if isloggedinuser(request.session):
        return redirect(f'/direct_messages/{church.id}')
    elif isloggedinchurch(request.session):
        return redirect(f'/direct_messages/{user.id}')
    else:
        return redirect('/')

def direct_messages(request, user_id):
    userobj=User.objects.get(id=user_id)
    if isloggedinchurch(request.session):
        church_id=request.session.get("church_id", "invalid")
        churchobj=Church.objects.get(id=church_id)
        dm = DirectMessages.objects.filter(user=userobj, church=churchobj)
    else:
        dm = DirectMessages.objects.filter(user=userobj)
    context={
        'one_user': userobj,
        'dm': dm
    }
    return render(request, "user/direct_messages.html", context)

def church_direct_messages(request, church_id):
    churchobj=Church.objects.get(id=church_id)
    if isloggedinuser(request.session):
        user_id=request.session.get("user_id", "invalid")
        userobj=User.objects.get(id=user_id)
        dm = DirectMessages.objects.filter(user=userobj, church=churchobj)
    else:
        dm = DirectMessages.objects.filter(church=churchobj)
    context={
        'one_church': churchobj,
        'dm': dm,
        'all_users': User.objects.all
    }
    return render(request, "church/church_direct_messages.html", context)

def church_add_message(request):
    church=Church.objects.get(id=request.session['church_id'])
    message = ChurchMessage.objects.create(message=request.POST['message'], church=church)
    return redirect('/church_home_page')

def delete(request, message_id):
    message=UserMessage.objects.get(id=message_id)
    message.delete()
    return redirect('/user_home_page')

def delete_church_message(request, message_id):
    message=ChurchMessage.objects.get(id=message_id)
    message.delete()
    return redirect('/church_home_page')

def delete_church(request, church_id):
    church=Church.objects.get(id=church_id)
    church.delete()
    return redirect('/user_home_page')

def church_home_page(request):
    context={
        'all_churches': Church.objects.all(),
        'all_users': User.objects.all(),
        'all_messages': ChurchMessage.objects.all(),
        'user_message': UserMessage.objects.all(),
        'all_comments': ChurchComments.objects.all(),
    }
    return render(request, "church_home_page.html", context)

def home_page(request):
    context={
        'all_churches': Church.objects.all(),
        'all_users':User.objects.all(),
        'all_messages':UserMessage.objects.all(),
        'all_comments':UserComments.objects.all()
    }
    return render(request, "home_page.html", context)

def edit_church(request, church_id):
    context={
        'one_church': Church.objects.get(id=church_id)
    }
    return render(request, "church/edit_church.html", context)

def edit_user(request, user_id):
    context={
        'one_user': User.objects.get(id=user_id)
    }
    return render(request, "user/edit_user.html", context)

def edit(request, church_id):
    edit = Church.objects.get(id=church_id)
    edit.address= request.POST['address']
    edit.church_city= request.POST['church_city']
    edit.church_state= request.POST['church_state']
    edit.website= request.POST['website']
    edit.facebook= request.POST['facebook']
    edit.instagram= request.POST['instagram']
    edit.church_email= request.POST['church_email']
    edit.church_phone= request.POST['church_phone']
    edit.denomination= request.POST['denomination']
    edit.values= request.POST['values']
    edit.size= request.POST['size']
    edit.youngest= request.POST['youngest']
    edit.younger=request.POST['younger']
    edit.young= request.POST['young']
    edit.old= request.POST['old']
    edit.oldest= request.POST['oldest']
    edit.other= request.POST['other']
    edit.save()
    return redirect(f'/church_profile/{church_id}')

def user_edit(request, user_id):
    edit = User.objects.get(id=user_id)
    edit.user_address=request.POST['user_address']
    edit.user_city=request.POST['user_city']
    edit.user_state=request.POST['user_state']
    edit.user_facebook=request.POST['user_facebook']
    edit.user_instagram=request.POST['user_instagram']
    edit.adults=request.POST['adults']
    edit.teens=request.POST['teens']
    edit.kids=request.POST['kids']
    edit.user_phone=request.POST['user_phone']
    edit.denomination=request.POST['denomination']
    edit.church_size=request.POST['church_size']
    edit.student_programs=request.POST['student_programs']
    edit.small_groups=request.POST['small_groups']
    edit.user_info_other=request.POST['user_info_other']
    edit.save()
    return redirect(f'/user_profile/{user_id}')

def church_add_comment(request, message_id):
    church = Church.objects.get(id=request.session['church_id'])
    message = ChurchMessage.objects.get(id=message_id)
    comment = ChurchComments.objects.create(comment=request.POST['comment'], church=church, wall_message=message)
    return redirect('/church_home_page')

def user_add_comment(request, message_id):
    user = User.objects.get(id=request.session['user_id'])
    message = UserMessage.objects.get(id=message_id)
    comment = UserComments.objects.create(comment=request.POST['comment'], user=user, wall_message=message)
    return redirect('/user_home_page')

def delete_comment(request, comment_id):
    comment=UserComments.objects.get(id=comment_id)
    comment.delete()
    return redirect('/user_home_page')

def delete_church_comment(request, comment_id):
    comment=ChurchComments.objects.get(id=comment_id)
    comment.delete()
    return redirect('/church_home_page')

def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'user_reg/user_info_other.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'user_reg/user_info_other.html', {'form': form})

def local_people(request):
    context={
        'local_person': User.objects.all()
    }
    return render(request, "local_people.html", context)

def area_churches(request):
    context={
        'area_church': Church.objects.all()
    }
    return render(request, "area_churches.html", context)

