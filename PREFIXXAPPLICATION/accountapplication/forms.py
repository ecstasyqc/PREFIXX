# import forms in forms.py

from django import forms
from django.contrib.auth.models import User
from .models import Profile

# creating main class ( LOGIN FORM )
class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput,
                               max_length=50)
    scndpassword = forms.CharField(label='Repeat Password',
                                    widget=forms.PasswordInput,
                                    max_length=50)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

    def scnd_clean_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['scndpassword']:
            raise forms.ValidationError("Passwords don't match")
        return cd['scndpassword']

class UserEditForm(forms.ModelForm):
        class Meta:
            model = User
            fields = ['first_name', 'last_name', 'email']
class ProfileEditForm(forms.ModelForm):
        class Meta:
            model = Profile
            fields = ['date_of_birth', 'photo']