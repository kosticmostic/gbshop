from django.shortcuts import render, HttpResponseRedirect
from .forms import ShopUserLoginForm, RegisterForm, UpdateForm
from django.contrib import auth
from django.urls import reverse
from django.http import HttpResponse, HttpRequest


def login(request: HttpRequest):
    tittle = 'вход'

    login_form = ShopUserLoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('index'))

    content = {'tittle': tittle, 'login_form': login_form}

    return render(request, 'authapp/login.html', content)


def logout(request: HttpRequest):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request: HttpRequest):
    tittle = 'регистрация'

    if request.method == 'POST':
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))

    else:
        register_form = RegisterForm()

    content = {
        'tittle': tittle,
        'reg_form': register_form
    }
    return render(request, 'authapp/register.html', content)


def edit(request: HttpResponse):
    tittle = 'профиль'

    if request.method == 'POST':
        update_form = UpdateForm(request.POST, instance=request.user)

        if update_form.is_valid():
            update_form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        update_form = UpdateForm(instance=request.user)

    content = {
        'tittle': tittle,
        'update_form': update_form
    }

    return render(request, 'authapp/edit.html', content)

