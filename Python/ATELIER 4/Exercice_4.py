"""
Exercice 4 de l'atelier 4 : Mots croisés
file       = "Exercice_4.py"
author     = "Baptiste Varamo & Jean-François Giammari"
credits    = ["Baptiste Varamo","Jean-François Giammari"]
version    = "1.0"
"""

from Exercice_2 import dictionnaire, mots_Nlettres


def mot_correspond(mot: str, motif: str) -> bool:
    """
    Check if the  string may or may not match the given pattern  string
    mot -- The word
    motif -- The pattern
    return True if match
    """
    is_matching = True
    if len(mot) != len(motif):
        is_matching = False
    else:
        length = len(mot)
        i = 0
        while i < length and is_matching:
            if motif[i] != "." and mot[i] != motif[i]:
                is_matching = False
            i += 1

    return is_matching


def presente(lettre: str, mot: str) -> int:
    """
    Define the place of a letter in a word
    mot -- The word
    lettre -- The letter
    return index or -1 if the letter dont exist in the word
    """
    return mot.find(lettre)


def mot_possible(mot: str, lettres: str) -> bool:
    """
    Define if the word is writable with the letters
    mot -- The word
    lettres -- The letters
    return True if is writable
    """
    is_matching = True
    length = len(mot)
    i = 0
    while i < length and is_matching:
        if lettres.find(mot[i]) == -1:
            is_matching = False
        else:
            lettres = lettres.replace(mot[i], '', 1);
        i += 1

    return is_matching


def mot_optimaux(dico: str, lettres: str) -> list:
    """
    Define the list of possible word with the letters
    dico -- The dictionnary
    lettres -- The letters usable
    return list of possible word
    """
    dico = dictionnaire(dico)
    lst_playable = []
    length = len(lettres)
    for i in range(length, 0, -1):
        lst_NFiltered = mots_Nlettres(dico, i)
        for e in lst_NFiltered:
            if mot_possible(e,lettres):
                lst_playable.append(e)

    return lst_playable


def test_exercice4():
    """
    Test for exercice 4
    """
    print("Test mot_correspond TRUE (cheval c..v.l) : ", mot_correspond("cheval", "c..v.l"))
    print("Test mot_correspond FALSE (cheval c..v..l) : ", mot_correspond("cheval", "c..v..l"))
    print("Test presente 2 (e,cheval) : ", presente("e", "cheval"))
    print("Test presente -1 (x,cheval) : ", presente("x", "cheval"))
    print("Test mot_possible TRUE (lapin, abilnpq) : ", mot_possible("lapin", "abilnpq"))
    print("Test mot_possible FALSE (cheval, abilnpq) : ", mot_possible("cheval", "abilnpq"))
    print("Test mot_possible TRUE (chapeau, abcehpuva): ", mot_possible("chapeau", "abcehpuva"))
    print("Test mot_possible FALSE (chapeau, abcehpuv) : ", mot_possible("chapeau", "abcehpuv"))
    print("Test mot_optimaux : ", mot_optimaux("littre.txt", "chipeau"))


test_exercice4()
