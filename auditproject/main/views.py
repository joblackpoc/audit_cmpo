from email import message
from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib import messages

def home(request):
    return render(request, 'main/home.html')

def registeruser(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'บัญชีของคุณ'-{username}-'สร้างเสร็จแล้ว')
            return redirect(request, 'main/login')
    form = UserRegisterForm()
    context = {
        'form':form,
    }
    return render(request, 'main/register.html',context)

