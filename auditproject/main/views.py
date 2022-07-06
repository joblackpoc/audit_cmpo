from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from main.forms import UserRegisterForm

# Create your views here.
def Register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'บัญชีของคุณ - {username} - สร้างเสร็จแล้ว')
            return redirect('login')
        else:
            form = UserRegisterForm()
        return render(request, 'main/register.html', {'form':form})

