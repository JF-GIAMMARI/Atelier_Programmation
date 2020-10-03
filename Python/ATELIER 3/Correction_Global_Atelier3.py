"""
Correction global Atelier 3
"""

"""
Exercice 1 de l'atelier 3 : Calculs, Comptage, Maximum, Fonction Entières, Structure itératives
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
    number_list -- List of  number to sum
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

#######################################################

"""
Exercice 2 de l'atelier 3 : Séparation
"""


def positionv2(L: list, e: int) -> int:
    """
     Cherche l'element e dans la liste L

     Keyword Arguments:
     L -- Liste d'entier
     e -- Element à chercher

     Return:
     Retourne l'indexe correspondant à la premiere itération de e
     """
    index = -1
    for i in range(len(L)):
        if L[i] == e:
            index = i

    return index


def position(L: list, e: int) -> int:
    """
    Cherche l'element e dans la liste L

    Keyword Arguments:
    L -- Liste d'entier
    e -- Element à chercher

    Return:
    Retourne l'indexe correspondant à la premiere itération de e
    """

    index = -1
    i = 0
    while i < len(L) and index == -1:
        if L[i] == e:
            index = i
        i += 1

    return index


def nb_occurence(L: list, e: int) -> int:
    """
    Compte le nombre de fois ou l'element e apparait dans la liste

    Keyword Arguments:
    L -- Liste d'entier
    e -- Element à chercher
    """

    occurence = 0
    for el in L:
        if el == e:
            occurence += 1

    return occurence


def est_trieev2(L: list) -> bool:
    """
    Vérifie si la liste est triée par ordre croissant

    Keyword arguments:
    L -- Liste à verifier
    """

    trie = True
    previous = None
    for e in L:
        if previous is not None and e < previous:
            trie = False
        previous = e

    return trie


def est_triee(L: list) -> bool:
    """
    Vérifie si la liste est triée par ordre croissant

    Keyword arguments:
    L -- Liste à verifier
    """

    trie = True
    i = 0
    length = len(L)
    while i < length and trie:
        if i + 1 < length and L[i + 1] < L[i]:
            trie = False

        i += 1

    return trie


def position_tri(L: list, e: int) -> int:
    """
    Cherche l'element e dans la liste L

    Keyword Arguments:
    L -- Liste d'entier triée
    e -- Element à chercher

    Return:
    Retourne l'indexe correspondant  à la premiere itération de e
    """
    debut = 0
    fin = len(L) - 1
    milieu = fin // 2
    index = None

    while debut < fin and index is None:
        if e == L[milieu]:
            index = milieu
        elif e > L[milieu]:
            debut = milieu + 1
        elif e < L[milieu]:
            fin = milieu - 1
        else:
            index = -1
        milieu = (fin - debut) // 2 + debut

    return index


def a_repetitions(L: list) -> bool:
    """
    Verifie si il y a des repetitions dans la liste

    Keyword Arguments:
    L -- Liste d'entier
    return bool
    """

    els = []
    repet = False
    i = 0
    length = len(L)
    while i < length and (not repet):
        if L[i] in els:
            repet = True
        else:
            els.append(L[i])

    return repet


#######################################################

"""
Exercice 3 de l'atelier 3 : Séparation
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

####################################################

"""
Exercice 4 de l'atelier 3 : fonctions - histogramme
"""

from Exercice_1 import val_max
import matplotlib.pyplot as plt


def histo(F_list: list, display_console: bool = False, display_gui: bool = False) -> list:
    """
    Transform if a list representing a function in a  histogram
    Keyword argument:
    F_list -- List of number
    display_console -- Bool for active the console displaying
    display_gui -- Bool for active the GUI displaying
    return a histogram list
    """
    MAXVALEUR = len(F_list)
    H_list = []
    for i in range(MAXVALEUR):
        H_list.append(F_list.count(i))

    """ OR 
       MAXVALEUR = max(F_list)
       H: list = [0]*(MAXVALEUR+1)
       for i in F_list:
           H[i] += 1
    """

    if display_console:
        afficheHisto(H_list)

    if display_gui:
        afficheHistoGUI(F_list)
    return H_list


def afficheHisto(H_list: list):
    """
    Display on console an histogram
    Keyword argument:
    H_list -- List of number to display (histogram)
    """
    print("\n\nHISTOGRAMME :")
    MAX0CC = val_max(H_list)
    length = len(H_list)
    for i in range(MAX0CC, 0, -1):
        for e in H_list:
            if e > 0 and e >= i:
                print("  # ", end="")
            else:
                print("    ", end="")
        print("")

    for i in range(length):
        print("|---", end="")
    print("|")

    for i in range(length):
        print("  " + str(i) + " ", end="")


def afficheHistoGUI(F_list: list):
    """
    Display on console an histogram
    Keyword argument:
    H_list -- List of number to display (histogram)
    """
    plt.hist(F_list, rwidth=0.80)
    plt.show()


def est_injective(F_list: list) -> bool:
    """
    Define if a list representing a function is injective
    Keyword argument:
    F_list -- List of number
    return true if is injective
    """
    H_list = histo(F_list)
    length = len(H_list)

    is_injective = True
    i = 0
    while i < length and is_injective:
        if H_list[i] > 1:
            is_injective = False
        i += 1

    return is_injective


def est_surjective(F_list: list) -> bool:
    """
    Define if a list representing a function is surjective
    Keyword argument:
    F_list -- List of number
    return true if is surjective
    """
    H_list = histo(F_list)
    length = len(H_list)

    is_surjective = True
    i = 0
    while i < length and is_surjective:
        if H_list[i] < 1:
            is_surjective = False
        i += 1

    return is_surjective


def est_bijective(F_list: list) -> bool:
    """
    Define if a list representing a function is bijective
    Keyword argument:
    F_list -- List of number
    return true if is bijective
    """

    return est_surjective(F_list) and est_injective(F_list)


def test_exercice4():
    """
    Test for exercice 4
    """
    print("\nTest pour histo [0, 1, 1, 0, 1, 2, 2, 0] :", histo([6, 5, 6, 8, 4, 2, 1, 5], True, True))
    print("\nTest pour Injective True :", est_injective([3, 0, 6, 7, 4, 2, 1, 5]))
    print("\nTest pour Injective False :", est_injective([6, 5, 6, 7, 4, 2, 1, 5]))
    print("\nTest pour Surjective True :", est_surjective([3, 0, 6, 7, 4, 2, 1, 5]))
    print("\nTest pour Surjective False :", est_surjective([6, 5, 6, 7, 4, 2, 1, 5]))
    print("\nTest pour Bijective True :", est_bijective([3, 0, 6, 7, 4, 2, 1, 5]))
    print("\nTest pour Bijective False :", est_bijective([6, 5, 6, 7, 4, 2, 1, 5]))


test_exercice4()

####################################################
