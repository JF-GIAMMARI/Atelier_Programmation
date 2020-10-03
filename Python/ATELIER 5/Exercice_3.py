"""
Exercice 3 de l'atelier 5 : Choix aléatoire d'un élément dans uen liste
file       = "Exercice_3.py"
author     = "Baptiste Varamo & Jean-François Giammari"
credits    = ["Baptiste Varamo","Jean-François Giammari"]
version    = "1.0"
"""

from random import *
from typing import *


def choose_element_list(list_in_which_to_choose: list[Any]) -> Any:
    """
    Picking a random element in a list
    list_in_which_to_choose -- The list
    :return: The element selected in the list
    """
    index = randint(0, len(list_in_which_to_choose) - 1)
    return list_in_which_to_choose[index]


def test_exercice3():
    """
    Test for Exercice 3
    """
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in range(5):
        print(choose_element_list(test_list), end=" / ")


test_exercice3()
