"""
Exercice 2 de l'atelier 5 : Mélange d'une liste
file       = "Exercice_2.py"
author     = "Baptiste Varamo & Jean-François Giammari"
credits    = ["Baptiste Varamo","Jean-François Giammari"]
version    = "1.0"
"""

from random import *


def mix_list(list_to_mix: list) -> list:
    """
    Mixing a list randomly
    list_to_mix -- The list
    :return: The mixed list
    """
    mixed_list = list_to_mix[:]
    for i in range(len(mixed_list)):
        j = randint(i, len(mixed_list) - 1)
        mixed_list[i], mixed_list[j] = mixed_list[j], mixed_list[i]
    return mixed_list


def test_exercice2(ord_list: list, nbr_try: int):
    """
    Test for Exercice 2
    """
    print(ord_list, " <-- LIST ORDONNEE")
    for i in range(nbr_try):
        mixed_list = mix_list(ord_list)
        if ord_list != mixed_list:
            print(mixed_list, " --> Mélange reussi")
        else:
            print(mixed_list, " --> Mélange échoué")


#test_exercice2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
