from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

from allauth.account.forms import SignupForm,LoginForm
from django import forms


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')

    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget = forms.TextInput(attrs={'placeholder': 'Email','type': 'email', 'class': 'form-control'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': 'Password','type': 'password','class': 'form-control'})
        self.fields['first_name'].widget = forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'})
        self.fields['last_name'].widget = forms.PasswordInput(attrs={'type': 'text','placeholder': 'Last Name','class': 'form-control'})

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user


class CustomLoginForm(LoginForm):
    # login = forms.CharField(max_length=30, label='First Name')
    # password = forms.CharField(max_length=30, label='Last Name')
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget = forms.TextInput(attrs={'type': 'email', 'class': 'form-control'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'type': 'password', 'class': 'form-control'})




# class UserRegisterForm(UserCreationForm):
#     first_name = forms.CharField(max_length=30, required=False, help_text='Required')
#     last_name = forms.CharField(max_length=30, required=False, help_text='Required')
#     email = forms.EmailField(help_text='Required')
#
#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
