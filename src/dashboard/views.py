from django.shortcuts import render, get_object_or_404
from dashboard.models import Employee
from .models import Employee
from django.http import HttpResponse

# Create your views here.
#elle permet de recuperer tous les employees de la base de donnee
def index(request):
    employees = Employee.objects.all()
    return render(request, "dashboard/impot.html", context={"employees": employees})

def details(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'dashboard/details.html', {'employee': employee})

def inf_employe(request):
    return render(request, "dashboard/inf_employe.html", {})

def impot_salaire(request):
    return render(request, "dashboard/impot_salaire.html", {})