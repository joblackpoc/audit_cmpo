from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, DocumentForm
from django.contrib.auth.models import User
from .models import Document
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

class home(ListView):
    model = Document
    template_name = 'main/home.html'

def registeruser(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'บัญชีของคุณ'-{username}-'สร้างเสร็จแล้ว')
            return redirect(request, 'login')
    form = UserRegisterForm()
    context = {
        'form':form,
    }

    return render(request, 'main/register.html',context)

@login_required
def profile_info(request,id):
    if request.method == 'POST':
        user = request.user.id
        return render(request=user)
    return render(request,'main/profile_info.html',user)

@login_required
def profile(request):
    profile_form = UserUpdateForm
    if request.method == 'POST':
        profile_form = UserUpdateForm(request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'บัญชีของคุณได้รับการปรับปรุงเรียบร้อย')
            return redirect('profile_info')
    profile_form = {
        'profile_form':profile_form
    }

    return render(request, 'main/profile.html', profile_form)

@login_required
def document_input(request):

    form = DocumentForm
    if request.method == 'POST':
        form = DocumentForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
    
    context = {
        'form':form
    }

    return render(request, 'main/document_input.html', context)

