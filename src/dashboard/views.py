from django.shortcuts import render, get_object_or_404, redirect
from dashboard.models import Employee
from .models import Employee
from .forms import EmployeeForm
from django.http import HttpResponse
from .utils import calcul_impot
from django.contrib.auth.decorators import login_required


# Create your views here.
#elle permet de recuperer tous les employees de la base de donnee
@login_required(login_url='/login_view/')
def index(request):
    employees = Employee.objects.all()
    total_employees = employees.count()
    return render(request, "dashboard/impot.html", context={"employees": employees, 'total_employees': total_employees})

@login_required(login_url='/login_view/')
def details(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    
    # Récupérez les données nécessaires de l'objet employee
    salaire = employee.salary
    is_maried = employee.is_marie
    children = employee.children

    # Calcul de l'impôt
    impot_annuel = calcul_impot(salaire, is_maried, children)

    # Convertissez les impôts en float après les avoir calculés
    impot_annuel = float(impot_annuel)
    # impot_mensuel = float(impot_mensuel)

    # Ajoutez l'impôt calculé au contexte de rendu
    context = {
        'employee': employee,
        'impot_annuel': impot_annuel,
        # 'impot_mensuel': impot_mensuel,
    }
    return render(request, 'dashboard/details.html', context)

@login_required(login_url='/login_view/')
def inf_employe(request):
    return render(request, "dashboard/inf_employe.html", {})

@login_required(login_url='/login_view/')
def impot_salaire(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, "dashboard/impot_salaire.html", {'form': form})

@login_required(login_url='/login_view/')
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

@login_required(login_url='/login_view/')
def delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('index')
    return render(request, 'dashboard/delete.html', {'object': employee})
