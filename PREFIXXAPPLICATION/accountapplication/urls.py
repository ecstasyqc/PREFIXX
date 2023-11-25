from django.urls import path
from django.urls import include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    # PATHES TO WORK IT :
    path('', views.dashboard, name='dashboard'),
    path('', include('django.contrib.auth.urls')),

    # PATHES TO REGISTRATION :
    path('registration/', views.RegistrationFunc, name='registration'),

    # PATH TO DELETE ACCOUNT :
    path('delete_account/', views.AccountDelete, name='delete_account'),
    path('delete_account_done/', views.AccountDeleteDone, name='delete_account_done'),

    # PATH TO EDIT ACCOUNT :
    path('edit/', views.Edit, name='edit'),
]