from django.shortcuts import render, HttpResponseRedirect
from .forms import ShopUserLoginForm
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
    return HttpResponseRedirect(reverse('main'))
