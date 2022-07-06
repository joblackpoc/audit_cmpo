from cProfile import label
from dataclasses import field
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from main.models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')
        labels = {
            'username':'Username',
            'first_name':'ชื่อจริง',
            'last_name':'นามสกุล',
            'email':'Email',
            'password1':"Password 8 ตัวอักษรขึ้นไปและห้ามใช้ตัวเลขอย่างเดียว",
            'password2':"ยืนยัน Password อีกครั้ง"
        }

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'first_name','last_name','email')
        labels = {
            'username':'Username','first_name':'ชื่อจริง','last_name':'นามสกุล','email':'Email'
        }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('section','user_phone','image')
        labels = {
            'section':'กลุ่มงาน','user_phone':'เบอร์โทรศัพท์','image':'รูปภาพของคุณ'
        }