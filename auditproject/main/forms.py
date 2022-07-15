from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import  Document, Profile
from ckeditor.widgets import CKEditorWidget

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')
        labels = {
            'username':'Username',
            'first_name':'ชื่อจริง',
            'last_name':'นามสกุล',
            'email':'Email ที่สามารถติดต่อได้',
            'password1':'Password 8 ตัวอักษรขึ้นไปและห้ามใช้ตัวเลขอย่างเดียว',
            'password2':'ยืนยัน Password อีกครั้ง'
        }

class UserUpdateForm(UserChangeForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields =('first_name','last_name','email')
        labels = {
            'first_name':'ชื่อจริง'
            ,'last_name':'นามสกุล'
            ,'email':'อีเมล์ที่สามารถติดต่อได้',
        }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('section','phone','picture')
        labels = {
            'section':'กลุ่มงาน/งาน'
            ,'phone':'เบอร์โทรศัพท์'
            ,'picture':'รูปภาพประจำตัว'
        }

class DocumentForm(forms.ModelForm):
    content = forms.CharField(required=False,widget=CKEditorWidget(attrs={'placeholder':'คำอธิบายเนื้อหาโดยละเอียด'}))
    class Meta:
        model = Document
        fields = ('title','section','shortnote','content','image','uploadfile')
        labels = {
            'title':'ชื่อเรื่อง'
            ,'section':'กลุ่มงาน/งาน'
            ,'shortnote':'คำอธิบายย่อ'
            ,'content':'เนื้อหาอย่างละเอียด'
            ,'image':'ภาพหน้าปก'
            ,'uploadfile':'ไฟล์ประกอบสำหรับให้ดาวน์โหลด'
        }
