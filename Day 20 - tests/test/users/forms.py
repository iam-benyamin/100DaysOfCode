from .models import User
from django import forms


class RegistartionForm(forms.ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = (
            'name',
            'last_name',
            'user_name',
            'email',
            'address',
            'remmeber_me',
            'password',
            'password2',
        )