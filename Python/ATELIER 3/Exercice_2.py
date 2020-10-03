"""
Exercice 2 de l'atelier 3 : Recherches, fonctions boolénnes, boucles while

file       = "Exercice_2.py"
author     = "Frau Axel & Jean-François Giammari"
credits    = ["Frau Axel","Jean-François Giammari"]
version    = "1.0"
"""


def position(L: list, e: int) -> int:
    """ Permet de trouver si un int e est contenue dans la liste L avec un for in classique """
    res = -1
    for i in range(0, len(L)):
        if e == L[i]:
            res = i
    return res


def positionB(L: list, e: int) -> int:
    """ Permet de trouver si un int e est contenue dans la liste L avec un while classique """
    end_while = False
    res = -1
    i = 0
    length = len(L)
    while not end_while or i > length:
        if L[i] == e:
            res = i
            end_while = True
        else:
            i += 1
    return res


def nb_occurriences_for(L: list, e: int) -> int:
    """ retourn le nombre de fois que le int 'e' apparait dans la liste 'L' """
    cpt = 0
    for i in range(0, len(L)):
        if L[i] == e:
            cpt += 1
    return cpt


def est_triee(L: list) -> bool:
    """ Verifie si une liste en triée dans l'ordre croissant ou non avec un for"""
    for i in range(0, len(L) - 1):
        if L[i] > L[i + 1]:
            res = False
    else:
        res = True
    return res


def est_triee_while(L: list) -> bool:
    """ Verifie si une liste en triée dans l'ordre croissant ou non avec un while"""
    lenght = len(L) - 1
    i = 0
    while i != lenght:
        if L[i] > L[i + 1]:
            return False
        else:
            i += 1
    return True


def position_tri(L: list, e: int) -> int:
    if not est_triee_while(L):
        L = sorted(L)
    start = 0
    end = len(L) - 1
    m = end // 2
    while start < end:
        if e == L[m]:
            return m
        elif e > L[m]:
            start = m + 1
        else:
            end = m - 1


print(position_tri([1, 2, 3, 4], 2))
# Pour est_triee :
# print(est_triee_for([1,1,3,4]))
# print(est_triee_while([1,5,3,4]))


# Pour nb_occurence :
# print(nb_occurrences([1,2,2,4], 2))

# Pour les fonctions position :
# result =  position([1,2,3,4], 2)
# result =  positionB([1,2,3,4], 2)
# if result != -1 :
#     print("Valeur à la position : {}".format(result+1) +" de la liste ou à L["+ str(result) +"]" )
# else :
#     print("Valeur non trouvée")
