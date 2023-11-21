from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # LAST LOGIN PATH :
    # path('login/', views.user_login, name='login')

    # NEW LOGIN & (NEW) LOGOUT PATHES :
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.dashboard, name='dashboard'),

    # (NEW) URL-PATHS TO CHANGE PASSWORDS :
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

]