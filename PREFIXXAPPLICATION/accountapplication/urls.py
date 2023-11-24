from django.urls import path
from django.urls import include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [

    # PATHES TO WORK IT :
    path('', views.dashboard, name='dashboard'),
    path('', include('django.contrib.auth.urls')),

    # PATHES TO REGISTRATION :
    path('registration/', views.register, name='registration')
]