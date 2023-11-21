# import all need modules for views.py :

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required

# there i write all main logic ^ code - to authenticate and login :

# create login_required decorator who try to login user :
@login_required
def dashboard(request):
    return render(request,
           'accountapplication/dashboard.html',
           {'section': 'dashboard'})

# create main function user_login :
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'accountapplication/login.html',
                  {'form': form})