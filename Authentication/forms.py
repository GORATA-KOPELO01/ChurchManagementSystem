from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
 
 
class CreationUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2','first_name', 'last_name']
 
class UpdateUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']