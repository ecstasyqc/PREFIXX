from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='home'),
    path('about/', views.about_page, name='about'),
    path('contacts/', views.contacts_page, name='contacts'),
]