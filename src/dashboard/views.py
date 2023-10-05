from django.shortcuts import render
from dashboard.models import Employee

# Create your views here.
#elle permet de recuperer tous les employees de la base de donnee
def index(request):
    employees = Employee.objects.all()
    return render(request, "dashboard/impot.html", context={"employees": employees})

def information_employe(request):
    return render(request, "dashboard/information_employe.html", {})