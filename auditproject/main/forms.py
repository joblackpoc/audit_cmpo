from dataclasses import field
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django_ckeditor_5.widgets import CKEditor5Widget
from matplotlib import widgets
from .models import *

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class':'focus:outline-none','placeholder':'demo@gmail.com'}))
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'focus:outline-none','placeholder':'user123'}))
    
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')
        labels = {
            'username':'Username',
            'first_name':'ชื่อจริง',
            'last_name':'นามสกุล',
            'email':'Email',
            'password1':'Password 8 ตัวอักษรขึ้นไปและห้ามใช้ตัวเลขอย่างเดียว',
            'password2':'ยืนยัน Password อีกครั้ง'
        }
    
    def save(self,commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class DocumentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields('content').required = False
    
    class Meta:
        model = Document
        fields = ('title','content','image','uploadfile')
        widgets = {
            'content': CKEditor5Widget(
                attrs={'class':'django_ckeditor_5'}, config_name='content'
            )
        }