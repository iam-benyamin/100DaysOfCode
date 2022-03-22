from .models import User
from django.forms import ModelForm


class RegistartionForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'