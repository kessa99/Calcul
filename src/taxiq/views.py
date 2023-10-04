from django.shortcuts import render

def home(request):
    return render(request, "page/home.html")

def aide(request):
    return render(request, "page/aide.html")

def informations(request):
    return render(request, "page/informations.html")

def services(request):
    return render(request, "page/services.html")

def login(request):
    return render(request, "page/login.html")

def signup(request):
    return render(request, "page/signup.html")