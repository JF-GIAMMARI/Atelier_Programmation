"""
Exercice 1 de l'atelier 5 : Génération de listes de nombre entiers aléatoires
file       = "Exercice_1.py"
author     = "Baptiste Varamo & Jean-François Giammari"
credits    = ["Baptiste Varamo","Jean-François Giammari"]
version    = "1.0"
"""

from random import *


def gen_list_random_int(int_nbr: int = 10, int_binf: int = 0, int_bsup: int = 10) -> list:
    """
    Generating a list of X random int between a range
    int_nbr -- The number of random int
    int_binf -- The min range limit (included)
    int_bsup -- The max range limit (excluded)
    :return: List of random int
    """
    random_list = []
    for i in range(int_nbr):
        random_list.append(randint(int_binf, int_bsup - 1))

    return random_list


def test_exercice1():
    """
    Test for Exercice 1
    """
    print("(5,5,10)      -> ", gen_list_random_int(5, 5, 10))
    print("(5,-50,10)    -> ", gen_list_random_int(2, -50, 10))
    print("(5,5,6)       -> ", gen_list_random_int(5, 5, 6))
    print("(int_bsup=30) -> ", gen_list_random_int(int_bsup=30))
    print("()            -> ", gen_list_random_int())


test_exercice1()
