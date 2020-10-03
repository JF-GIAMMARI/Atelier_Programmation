"""
Exercice 1 de l'atelier 3 : Calculs, Comptage, Maximum, Fonction Entières, Structure itératives

file       = "Exercice_1.py"
author     = "Frau Axel & Jean-François Giammari"
credits    = ["Frau Axel","Jean-François Giammari"]
version    = "1.0"
"""


def somme(number_list: list) -> int:
    """ Return the sum of a list
    Keyword argument:
    number_list -- List of number to sum
    """
    sum = 0
    for i in range(len(number_list)):
        sum += number_list[i]
    return sum


def sommev2(number_list: list) -> int:
    """ Return the sum of a list
    Keyword argument:
    number_list -- List of number to sum
    """
    sum = 0
    for e in number_list:
        sum += e
    return sum


def sommev3(number_list: list) -> int:
    """ Return the sum of a list
    Keyword argument:
    number_list -- List of number to sum
    """
    sum = 0
    length = len(number_list)
    i = 0
    while i < length:
        sum += number_list[i]
        i += 1
    return sum


def moyenne(number_list: list) -> float:
    """ Return the average of a list
    Keyword argument:
    number_list -- List of int
    """
    average = 0
    length = len(number_list)
    if length > 0:
        average = somme(number_list) / length
    return average


def nb_sup(number_list: list, e: int) -> int:
    """ Returns the number of value strictly superior of a value in a list
    Keyword argument:
    number_list -- List of number to sum
    e           -- The limit value
    returns the number of value strictly superior to e
    """
    result = 0
    for i in range(len(number_list)):
        if number_list[i] > e:
            result += 1
    return result


def nb_supv2(number_list: list, e: int) -> int:
    """ Returns the number of value strictly superior of a value in a list
    Keyword argument:
    number_list -- List of int
    e           -- The limit value
    returns the number of value strictly superior to e
    """
    result = 0
    for element in number_list:
        if element > e:
            result += 1
    return result


def moy_sup(number_list: list, e: int) -> float:
    """ Returns the average of all values strictly superior of a value in a list
    Keyword argument:
    number_list -- List of int
    e           -- The limit value
    """
    filter_list = []
    sum = 0
    count = 0
    result = 0
    for element in number_list:
        if element > e:
            sum += 1
            count += 1

    if count != 0:
        result = sum / count

    return result


def val_max(number_list: list) -> int:
    """ Returns the maximum value of a list
    Keyword argument:
    number_list -- List of int
    """
    max = number_list[0]
    for i in range(1, len(number_list)):
        if number_list[i] > max:
            max = number_list[i]

    return max


def ind_max(number_list: list) -> int:
    """ Returns the maximum index value of a list
    Keyword argument:
    number_list -- List of int
    """
    max = number_list[0]
    id = 0
    for i in range(1, len(number_list)):
        if number_list[i] > max:
            max = number_list[i]
            id = i

    return id

def test_exercice1():
    """ Test for Exercice 1 """
    S = [1, 10, 100, 1000, 10000]
    print("Test somme 1111 : ", somme(S))
    print("Test somme liste vide : ", somme([]))
    print("\nTest moyenne  2222.2:", moyenne(S))
    print("Test moyenne list vide 0:", moyenne([]))
    print("\nTest nombre_sup 2 :  ", nb_sup(S, 110))
    print("Test moyenne_sup : 5500 : ", moy_sup(S, 110))
    print("Test val max 10000 : ", val_max(S))
    print("Test index max 4 :", ind_max(S))


test_exercice1()
