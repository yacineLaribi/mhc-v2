from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    category = forms.ChoiceField(choices=CustomUser.USER_CATEGORIES)

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'category']
