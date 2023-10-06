from django.shortcuts import render, get_object_or_404, redirect
from dashboard.models import Employee
from .models import Employee
from .forms import EmployeeForm
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
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, "dashboard/impot_salaire.html", {'form': form})

def edit(request, pk):
    modif = get_object_or_404(Employee, pk=pk)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=modif)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirige vers la page d'index après la modification réussie
    else:
        form = EmployeeForm(instance=modif)

    return render(request, 'dashboard/edit.html', {'form': form})

def delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('index')
    return render(request, 'dashboard/delete.html', {'object': employee})
