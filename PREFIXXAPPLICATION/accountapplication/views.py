# import all need modules for views.py :

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm
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

                                                                    # CREATING REFISTRATION LOGIC ^ METHOD

def RegistrationFunc(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # CREATE NEW USER, BUT DON'T SAVE THEM TO DATABASE :
            new_user = user_form.save(commit=False)

            # SET VALID PASSWORD :
            new_user.set_password(user_form.cleaned_data['password'])

            # SAVE USER OBJECT :
            new_user.save()

            # RETURN GET HTML PAGE REGISTER WAS SUCCESSFUL
            return render(request, 'user_registration/registration_done.html',
                                         {'user_form': user_form})
    else:
        user_form = UserRegistrationForm()
        return render(request, 'user_registration/registration.html',
                                     {'user_form': user_form})

# CREATING DELETE ACCOUNT FORM

def AccountDelete(request, user_id):
    # delete the user from the database :
    user_delete = user.objects.get(id=user_id)
    user_delete.delete()

    # return a response to the user :
    return render(request, 'delete_account/delete_account.html')

def AccountDeleteDone(request):
    return render(request, 'delete_account/delete_account_done.html')