from django.shortcuts import render, redirect

def home(request):
    return render(request, "page/home.html")

def aide(request):
    return render(request, "page/aide.html")

def informations(request):
    return render(request, "page/informations.html")

def services(request):
    return render(request, "page/services.html")

def dashboard(request):
    return render(request, "dashboard.html")