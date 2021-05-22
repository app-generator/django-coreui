from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.template import RequestContext

from .forms import CreateUserForm
from klaim_registration.models import DaftarHRD

def RegistrationPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Akun '+user+' sudah berhasil dibuat')
            return redirect('login')
    else:
        
        context = {
            'form':form
        }
    return render(request, 'accounts/register.html',context)

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username)
        # print(password)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            is_hrd = DaftarHRD.objects.filter(user__username=username)
            if is_hrd:
                return redirect('hrd-klaim')
            else:
                return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect!')
    context = {}

    return render(request,'accounts/login.html', context)

def LogoutPage(request):
    logout(request)

    return redirect('login')