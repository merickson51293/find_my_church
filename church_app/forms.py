from django import forms 
from .models import UserPic
  
class ImageForm(forms.ModelForm): 
  
    class Meta: 
        model = UserPic
        fields = ['user_Img', 'user']