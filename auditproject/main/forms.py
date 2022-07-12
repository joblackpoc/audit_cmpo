from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import  Document

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

class UserUpdateForm(UserChangeForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields =('first_name','last_name','email')
        labels = {
            'first_name':'ชื่อจริง','last_name':'นามสกุล','email':'อีเมล์ที่สามารถติดต่อได้',
        }

class DocumentForm(forms.ModelForm):

    class Meta:
        model = Document
        fields = ('title','content','media','image','uploadfile')
        labels = {
            'title':'ชื่อเรื่อง','content':'เนื้อหา','media':'media','image':'ภาพประกอบชื่อเรื่อง','uploadfile':'แนบไฟล์ pdf,docx,xlsx,zip,rar'
        }
