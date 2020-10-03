"""
Exercice 4 de l'atelier 5 : Choix aléatoire de plusieur élément
file       = "Exercice_4.py"
author     = "Baptiste Varamo & Jean-François Giammari"
credits    = ["Baptiste Varamo","Jean-François Giammari"]
version    = "1.0"
"""

from random import *


def extract_elements_list(list_in_which_to_choose: list, int_nbr_of_element_to_extract: int) -> list:
    """
    Picking multiple random elements in a list
    list_in_which_to_choose -- The list
    int_nbr_of_element_to_extract -- The number of element to select randomly
    :return: The list of elements selected in the list
    """
    duplicated_list = list_in_which_to_choose[:]
    selected_list = []
    if int_nbr_of_element_to_extract < len(list_in_which_to_choose):
        for i in range(int_nbr_of_element_to_extract):
            index = randint(0, len(duplicated_list) - 1)
            selected_list.append(duplicated_list.pop(index))
    else:
        selected_list = duplicated_list[:]
    return selected_list


def test_exercice4():
    """
    Test for Exercice 4
    """
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(extract_elements_list(test_list, 2))
    print(extract_elements_list(test_list, 5))
    print(extract_elements_list(test_list, 2))
    print(extract_elements_list(test_list, 10))
    print(extract_elements_list(test_list, 100))


#test_exercice4()
