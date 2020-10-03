"""
Bilan de l'atelier 3 : Boucles
file       = "Bilan_JFGiammari.py"
author     = "Jean-François Giammari"
credits    = [""Jean-François Giammari"]
version    = "1.0"
"""


def fill_list(b_inf: int, b_sup: int, max_len: int) -> list:
    """
    Function that asks the user to enter one by one the elements of the
    the list by systematically checking that they are within limits.
    It should be able to enter a maximum of n items. There is no number
    minimum.

    b_inf -- The min value limit
    b_sup -- The max value limit
    max_len -- The max entry value limit
    :return: list of all valid entry
    """
    filled_list = []
    is_valid_int = True

    while len(filled_list) < max_len and is_valid_int:
        entry = input("Veuillez saisir un nombre entre {} et {} il reste {} places  : ".format(b_inf, b_sup,max_len - len(filled_list)))
        if entry.isdigit():  # If entry is a positive integer
            if b_inf <= int(entry) <= b_sup:
                filled_list.append(entry)
            else:
                is_valid_int = False

    return filled_list


def test_filllist():
    """
    Function for test  fill_list()
    """
    print("Fonction test avec fill_list(6,10,5) -> Entry: 6,10,11 --- [6,10] : ")
    print(fill_list(6, 10, 5))
    print("Fonction test avec fill_list(6,10,5) -> Entry: -1,6,11 --- [6] : ")
    print(fill_list(6, 10, 5))
    print("Fonction test avec fill_list(6,10,5) -> Entry: -1,g,6,11 --- [6] : ")
    print(fill_list(6, 10, 5))
    print("Fonction test avec fill_list(6,10,5) -> Entry: 11 --- [] : ")
    print(fill_list(6, 10, 5))
    print("Fonction test avec fill_list(6,10,2) -> Entry: 6,10 --- [6,10] : ")
    print(fill_list(6, 10, 2))


test_filllist()
