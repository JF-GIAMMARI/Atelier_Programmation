# Auteur : Jean-François Giammari & Axel Frau
# Date : 08/09/2020
# Version : 1
# Description : Calcul de Dates
import datetime

import Exercice_2

# EXERCICE 4
"""
Cet ensemble de fonction nous permet de verifier au final si une personne est majeur ou non, on va faire 
appelle a une fonction depuis un autre fonction pour tester la validité des données saisies.

date_est_valide() => permet de verifier si la date est bonne ou non.
saisie_date_naissance() => permet de prendre un jour, un mois, et une année et de renvoyer un objet de type date a partir de ces données.
age() => permet de calculer l'age d'une personne à partir d'une date
est_majeur() => permet de verifier a partir de l'age si la personne est majeur ou non.


"""


def date_est_valide(day, month, year):
    # Définition des constantes :
    MAX_MONTH = 12
    MIN_GENERAL = 1
    MAX_DAY_BISSEXTILE = 29
    MAX_DAY_NON_BISSEXTILE = 28
    MAX_DAY_EVEN = 30
    MAX_DAY_ODD = 31
    FEBRUARY = 2
    JULY = 7

    res = True
    # Verifie la validité du mois entré
    if month > MAX_MONTH or month < MIN_GENERAL:
        return False

    # On vérifie si l'année rentrée est bisextille et que le mois rentrée est le mois de février
    if Exercice_2.est_bissextile(year) and month == FEBRUARY:
        if day > MAX_DAY_BISSEXTILE or day < MIN_GENERAL:
            res = False

    elif not Exercice_2.est_bissextile(year) and month == FEBRUARY:
        if day > MAX_DAY_NON_BISSEXTILE or day < MIN_GENERAL:
            res = False

    else:
        if (not (month % 2) and month != JULY) and (
                day > MAX_DAY_ODD or day < MIN_GENERAL):  # On verifie la validité du nombre du jour rentré pour un mois de 30 jours
            res = False
        elif ((month % 2) and month != JULY) and (
                day > MAX_DAY_EVEN or day < MIN_GENERAL):  # On verifie la validité du nombre du jour rentré pour un mois de 31 jours
            res = False

    return res


def saisie_date_naissance(day: int, month: int, year: int) -> datetime.date or bool:
    if date_est_valide(day, month, year):
        return datetime.date(year, month, day)
    else:
        return False


def age(birthdate: datetime.date) -> int:
    today = datetime.datetime.today()
    # Comme false = 0 et true = 1 alors je l'utilise pour décrementer ou non l'age en fonction du mois et du jour.
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age


def est_majeur(birthdate: datetime.date):
    VALUE_MAJORITE = 18
    # Tout s'implement si l'age est au dessus de la constante fixer pour l'age (18ans en france sinon ça pourrait
    # être 21ans au étéat UNIS) alors return True
    return age(birthdate) >= VALUE_MAJORITE
    # if age(birthdate) >= VALUE_MAJORITE :
    #    return True
    # else :
    #    return False


def test_access():  # Fonction comparant le résultat obtenue et attendue dans les cas les plus significatif.
    date_is_valid = False
    while not date_is_valid:  # Tant que la date est invalide je redemande de rentrer les valeur.
        try:  # Dans le cas ou un caractère autre qu'une nombre/chiffre est rentrer je redemande les valeurs (permet d'éviter les crashs)
            day = int(input("Veuillez rentrer jour de naissance : "))
            month = int(input("Veuillez rentrer mois de naissance (en chiffre) : "))
            year = int(input("Veuillez rentrer année de naissance : "))
            date = saisie_date_naissance(day, month, year)
            if date == False:
                print('date invalide veuillez recommencer !')
            else:
                age_res = age(date)
                majeur_res = est_majeur(date)
                if majeur_res:
                    print("Bonjour, vous avez", age_res, "ans, Accès autorisé")
                else:
                    print("Désolé, vous avez", age_res, "ans, Accès interdit")
                date_is_valid = True
            pass
        except ValueError:  # C'est ici la gestion du cas où un autre caractère est rentrer qui ne serrais pas un chiffre ou un nombre.
            print("Il y eu une erreur recommencer s'il vous plait")
            pass

#Appel des fonctions
test_access() 


# Appel des fonctions
test_access()
