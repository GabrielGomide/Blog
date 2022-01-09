from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *

# Create your views here.
def login(request):
    error = False

    if request.method == 'POST':
        form = CreateAccount(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            if Account.objects.filter(username=username, password=password).exists():
                response = redirect('main')
                response.set_cookie('username', username)
                return response
            else:
                form = CreateAccount()
                error = True
    else:
        form = CreateAccount()

    context = {'form': form, 'error': error}

    return render(request, 'Authentication/login.html', context)

def signup(request):
    error = False

    if request.method == 'POST':
        form = CreateAccount(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            if not Account.objects.filter(username=username).exists():
                account = Account(username=username, password=password, can_post=False)
                account.save()
                response = redirect('main')
                response.set_cookie('username', username)
                return response
            else:
                form = CreateAccount()
                error = True
    else:
        form = CreateAccount()

    context = {'form': form, 'error': error}

    return render(request, 'Authentication/signup.html', context)

