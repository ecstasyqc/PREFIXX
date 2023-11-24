from django.urls import path
from django.urls import include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [

    #                                                                LAST LOGIN PATH :
    #  path('login/', views.user_login, name='login')
    #
    #                                                       NEW LOGIN & (NEW) LOGOUT PATHES :
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #
    #                                                       (NEW) URL-PATHS TO CHANGE PASSWORDS :
    # path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    # path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    #
    #                                                                 DASHBOART PATH :
    # path('', views.dashboard, name='dashboard'),
    #
    #                                                           PATHES FOR RESET PASSWORDS :
    # path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('password_reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    #
    #
    #                                                           NEW PATHES TO WORK IT :

    path('', views.dashboard, name='dashboard'),
    path('', include('django.contrib.auth.urls')),

]