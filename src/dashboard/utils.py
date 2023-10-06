#!/usr/bin/python3

from decimal import Decimal

def calcul_impot(salaire, is_maried, children):
    """
    Calcul de l'impôt annuel et mensuel en fonction du salaire, de l'état matrimonial et du nombre d'enfants.
    """
    
    salaire = Decimal(salaire)
    retenu = Decimal(0)
    impot = Decimal(0)  # Initialisation de la variable impot

    if is_maried:
        retenu += Decimal('0.1') * salaire  # 10% de retenue pour les personnes mariées

    if 0 < children <= 5:
        retenu += Decimal('0.02') * children * salaire  # 2% de retenue par enfant

    salaire_apres_retenue = salaire - retenu

    seuils = [
        (Decimal('900000'), Decimal('0')),
        (Decimal('3000000'), Decimal('0.05')),
        (Decimal('6000000'), Decimal('0.1')),
        (Decimal('9000000'), Decimal('0.15')),
        (Decimal('12000000'), Decimal('0.2')),
        (Decimal('15000000'), Decimal('0.25')),
        (Decimal('15000000'), Decimal('0.25'))
    ]

    for seuil, taux in seuils:
        if salaire_apres_retenue <= seuil:
            impot = taux * (salaire_apres_retenue - seuil) + retenu
            break

    impot_annuel = impot
    impot_mensuel = impot / Decimal('12')
    return impot_annuel, impot_mensuel
