"""
Exercice 3 de l'atelier 3 : Séparation
file       = "Exercice_3.py"
author     = "Frau Axel & Jean-François Giammari"
credits    = ["Frau Axel","Jean-François Giammari"]
version    = "1.0"
"""


def separer(number_list: list) -> list:
    """ Sort by sign function without ascending or descending sorting
    Keyword argument:
    number_list -- List of number to sum
    return the sorted list
    """
    LSEP = []
    count_negative = 0
    for e in number_list:
        if e < 0:
            LSEP.insert(0, e)
            count_negative += 1
        elif e > 0:
            LSEP.append(e)
        else:
            LSEP.insert(count_negative, e)
            
    return LSEP


def test_exercice3():
    """
    Test function for separer()
    """
    S = [35, -150, 0, -100, 15, -20, 0, 1200, 1]
    R = [-20, -100, -150, 0, 0, 35, 15, 1200, 1]

    print("\nAttendu : ", R)
    print("Résultat : ", separer(S))
    if separer(S) == R:
        print("Le test est un succès !")
    else:
        print("Le test est un echec")


test_exercice3()
