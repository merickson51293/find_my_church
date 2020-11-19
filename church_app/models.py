from django.db import models
import re, bcrypt

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
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()

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
    city_state=models.CharField(max_length=255)
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
    church= models.ForeignKey(Church, related_name='church_message', on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)