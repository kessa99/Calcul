from django.urls import path
from . import views

urlpatterns = [
    path('impot_salaire', views.impot_salaire, name='impot_salaire'),
    path('inf_employe', views.inf_employe, name='inf_employe'),
    path('index', views.index, name='index'),
    path('details/<int:pk>/', views.details, name='details'),
]

