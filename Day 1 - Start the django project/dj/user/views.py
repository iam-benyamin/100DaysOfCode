from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def static(request):
    return render(request, 'user/static.html')
