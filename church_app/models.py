from django.db import models
import re, bcrypt
from enum import Enum

class UserType(Enum):
    User = 1
    Church = 2

class UserManager(models.Manager):
    def validator(self, postdata):
        email_check=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        errors={}
        if len(postdata['first_name'])<2:
            errors['first_name']="First name must be longer than 2 characters!"
        if len(postdata['last_name'])<2:
            errors['last_name']="Last name must be longer than 2 characters!"
        if not email_check.match(postdata['email']):
            errors['email']="Email must be valid format!"
        if len(postdata['password'])<8:
            errors['password']="Password must be at least 8 characters!"
        if postdata['password'] != postdata['conf_password']:
            errors['conf_password']="Password and confirm password must match!"
        return errors
    def login_validator(self, postdata):
        errors = {}
        check = User.objects.filter(email=postdata['email'])
        if not check:
            errors['email'] = "Email has not been registered."
        else:
            if not bcrypt.checkpw(postdata['password'].encode(), check[0].password.encode()):
                errors['email'] = "Email and password do not match."
        return errors

class User(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    age=models.CharField(max_length=20)
    user_address=models.CharField(max_length=255)
    user_city=models.CharField(max_length=255)
    user_state=models.CharField(max_length=2)
    user_email=models.CharField(max_length=255)
    user_facebook=models.CharField(max_length=255)
    user_instagram=models.CharField(max_length=255)
    adults=models.CharField(max_length=255)
    teens=models.CharField(max_length=255)
    kids=models.CharField(max_length=255)
    user_phone=models.CharField(max_length=255)
    denomination=models.CharField(max_length=255)
    # catholic=models.CharField(max_length=255)
    # nondenominational=models.CharField(max_length=255)
    # baptist=models.CharField(max_length=255)
    # reformed=models.CharField(max_length=255)
    # lutheran=models.CharField(max_length=255)
    # methodist=models.CharField(max_length=255)
    # pentecostal=models.CharField(max_length=255)
    # other=models.CharField(max_length=255)
    # no_preference=models.CharField(max_length=255)
    church_size=models.CharField(max_length=255)
    student_programs=models.CharField(max_length=255)
    small_groups=models.CharField(max_length=255)
    user_info_other=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()

class UserPic(models.Model):
    user_Img=models.ImageField(upload_to='images')
    user=models.ForeignKey(User, related_name="user_pic", on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class ChurchManager(models.Manager):
    def church_validator(self, postdata):
        email_check=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        errors={}
        if len(postdata['church_name'])<5:
            errors['church_name']="First name must be longer than 5 characters!"
        if len(postdata['admin_name'])<5:
            errors['admin_name']="Admin name must be longer than 5 characters!"
        if not email_check.match(postdata['admin_email']):
            errors['admin_email']="Email must be valid format!"
        if len(postdata['password'])<8:
            errors['password']="Password must be at least 8 characters!"
        if postdata['password'] != postdata['conf_password']:
            errors['conf_password']="Password and confirm password must match!"
        return errors
    def church_login_validator(self, postdata):
        errors = {}
        check = Church.objects.filter(admin_email=postdata['admin_email'])
        if not check:
            errors['admin_email'] = "Admin email has not been registered."
        else:
            if not bcrypt.checkpw(postdata['password'].encode(), check[0].password.encode()):
                errors['admin_email'] = "Admin email and password do not match."
        return errors

class Church(models.Model):
    church_name=models.CharField(max_length=255)
    admin_name=models.CharField(max_length=255)
    admin_email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    church_city=models.CharField(max_length=255)
    church_state=models.CharField(max_length=2)
    address=models.CharField(max_length=255)
    website=models.CharField(max_length=255)
    facebook=models.CharField(max_length=255)
    instagram=models.CharField(max_length=255)
    twitter=models.CharField(max_length=255)
    church_email=models.CharField(max_length=255)
    church_phone=models.CharField(max_length=13)
    denomination=models.CharField(max_length=255)
    values=models.TextField()
    size=models.CharField(max_length=255)
    youngest=models.CharField(max_length=255)
    younger=models.CharField(max_length=255)
    young=models.CharField(max_length=255)
    old=models.CharField(max_length=255)
    oldest=models.CharField(max_length=255)
    other=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=ChurchManager()

class Pastor(models.Model):
    pastor_name=models.CharField(max_length=255)
    pastor_title=models.CharField(max_length=255)
    pastor_phone=models.CharField(max_length=13)
    pastor_email=models.CharField(max_length=255)
    pastor_social=models.CharField(max_length=255)
    church=models.ManyToManyField(Church, related_name="church_pastor")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Message(models.Model):
    message=models.TextField()
    church= models.ForeignKey(Church, related_name='church_message', on_delete=models.CASCADE, null=True)
    user= models.ForeignKey(User, related_name='user_message', on_delete=models.CASCADE, null=True)
    user_type= models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class DirectMessages(models.Model):
    church=models.ForeignKey(Church, related_name='user_dm', on_delete=models.CASCADE)
    user=models.ForeignKey(User, related_name='church_dm', on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class ChurchComments(models.Model):
    comment=models.CharField(max_length=255)
    church= models.ForeignKey(Church, related_name='church_comment', on_delete=models.CASCADE)
    wall_message= models.ForeignKey(Message, related_name='church_post_comments', on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class UserComments(models.Model):
    comment=models.CharField(max_length=255)
    user= models.ForeignKey(User, related_name='user_comment', on_delete=models.CASCADE)
    wall_message= models.ForeignKey(Message, related_name='user_post_comments', on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)