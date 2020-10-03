# Auteur : Jean-François Giammari & Axel Frau
# Date : 07/09/2020
# Version : 1
# Description : Résolution d'une équation du second degré

"""
Les inputs aurait pu être mis dans la fonction quitte à crée une fonction annexe dans ce seul but
"""
# Les inputs aurait pu être mis dans la fonction quitte à crée une fonction annexe dans ce seul but

# EXERCICE 3

import math


def discrimitant(a: float, b: float, c: float) -> float:
    """ 
     Cette fonction permet de calculer le discriminant
    """
    return b * b - (4 * a * c)


def racine_unique(a, b) -> float:
    """ 
     Cette fonction permet de calculer la racine unique
    """
    return (-1 * b) / (2 * a)


def racine_double(a: float, b: float, delta: float, num: float) -> float:
    """ 
     Cette fonction permet de calculer la racine double
    """
    result = 0
    if num == 1:
        result = ((-1 * b) + math.sqrt(delta)) / (2 * a)
    else:
        result = ((-1 * b) - math.sqrt(delta)) / (2 * a)

    return result


def str_equation(a: float, b: float, c: float):
    a = str(a)
    b = str(b)
    c = str(c)
    if int(a) == 1:
        a = "x2"
    elif int(a) == -1:
        a = "-x2"
    elif int(a) < -1:
        a = a + "x2"
    elif int(a) > 1:
        a = a + "x2"
    elif int(a) == 0:
        a = " "

    if int(b) == 1:
        b = " + x "
    elif int(b) == -1:
        b = " - x "
    elif int(b) < -1:
        b = " - " + str(int(b) * -1) + "x "
    elif int(b) > 1:
        b = " + " + b + "x "
    elif int(b) == 0:
        b = " "

    if int(c) > 1:
        c = "+ " + c
    elif int(c) == 0:
        c = " "
    elif int(c) < -1:
        c = " - " + str(int(c) * -1)

    return a + b + c


def solution_equation(a: float, b: float, c: float) -> float:
    discriminant = discrimitant(a, b, c)
    message = "Aucune solution réelle"
    if discriminant == 0:
        message = "Solution de l'équation : " + str_equation(a, b, c) + "\n Racine Unique = " + str(
            round(racine_unique(a, b), 2))
    elif discriminant > 0:
        message = "Solution de l'équation : " + str_equation(a, b, c) + "\n x1 = " + str(
            round(racine_double(a, b, discriminant, 1), 2)) + "\n x2 = " + str(
            round(racine_double(a, b, discriminant, 2), 2))

    print(message)


# Appel des fonctions
a = int(input('A : '))
b = int(input('B : '))
c = int(input('C : '))
solution_equation(a, b, c)
