from atexit import register
from django.shortcuts import render
from django.shortcuts import redirect

from .forms import RegistartionForm

def home(request):
    return render(request, 'home.html')

def user_registartion_view(request):
    if request.method == "POST":
        form = RegistartionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(home)
    else:
        form = RegistartionForm()

    return render(request, "register.html", {'form': form})