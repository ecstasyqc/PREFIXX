# import forms in forms.py

from django import forms

# creating main class ( LOGIN FORM )
class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
