#!/usr/bin/python3

from decimal import Decimal

def calcul_impot(salary, is_maried, children):

    """
    Calcul de l'impôt annuel et mensuel en fonction du salary, de l'état matrimonial et du nombre d'enfants.
    """
    retenu = 0
    impot = 0

    if is_maried:
        retenu += Decimal('0.1') * salary  # 10% de retenue pour les personnes mariées

    if 0 < children <= 5:
        retenu += Decimal('0.02') * children * salary  # 2% de retenue par enfant

    # Calcul des tranches d'imposition
    tranches = [(Decimal('0'), Decimal('900000')), (Decimal('900001'), Decimal('3000000')),
                (Decimal('3000001'), Decimal('6000000')), (Decimal('6000001'), Decimal('9000000')),
                (Decimal('9000001'), Decimal('12000000')), (Decimal('12000001'), Decimal('15000000'))]
    
    taux_imposition = [Decimal('0'), Decimal('0.05'), Decimal('0.1'), Decimal('0.15'), Decimal('0.2'), Decimal('0.25')]

    salaire_restant = salary - retenu

    for i, (limite_inf, limite_sup) in enumerate(tranches):
        if salaire_restant <= 0:
            break

        montant_tranche = min(salaire_restant, limite_sup) - limite_inf
        if montant_tranche > 0:
            impot += montant_tranche * taux_imposition[i]

        salaire_restant -= montant_tranche

    impot_annuel = impot
    impot_mensuel = impot_annuel / Decimal('12')

    return impot_annuel, impot_mensuel

# Exemple d'utilisation de la fonction
salary = Decimal('20000000')  # exemple de salaire (en Decimal)
is_married = True  # exemple de statut matrimonial
children = 2  # exemple de nombre d'enfants

impot_annuel, impot_mensuel = calcul_impot(salary, is_married, children)
print("Impôt annuel à payer :", impot_annuel)
print("Impôt mensuel à payer :", impot_mensuel)
