import datetime
from django.shortcuts import render, redirect
from .forms import ProfileUpdateForm, UserRegisterForm, UserUpdateForm, DocumentForm
from django.contrib.auth.models import User
from .models import Document, Profile, Sectionlist
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.core.paginator import Paginator

class home(ListView):
    model = Document
    template_name = 'main/home.html'
    context_object_name = 'document'
    paginate_by = 5

def registeruser(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            username = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'บัญชีของคุณ'-{username}-'สร้างเสร็จแล้ว')
            return redirect(request, 'login')
    form = UserRegisterForm()
    context = {
        'form':form,
    }

    return render(request, 'main/register.html',context)

@login_required
def profile(request):
    if request.method == 'POST':
      u_form = UserUpdateForm(request.POST, instance=request.user)
      p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

      if u_form.is_valid() and p_form.is_valid():
        u_form.save()
        p_form.save()
        messages.success(request, f'Your accout has been Update')
        return redirect('profile')
    else:
      u_form = UserUpdateForm(instance=request.user)
      p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
      'u_form': u_form,
      'p_form': p_form
    }
    return render(request, 'main/profile.html', context)

@login_required
def document_input(request):
    
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            fm = form.save(commit=False)
            fm.user = request.user
            fm.save()
        return redirect('home')
    else:
        form = DocumentForm()

    return render(request, 'main/document_input.html', {'form':form})
