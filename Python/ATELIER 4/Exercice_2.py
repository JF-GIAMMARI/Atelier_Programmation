"""
Exercice 2 de l'atelier 4 : Mots croisés
file       = "Exercice_2.py"
author     = "Baptiste Varamo & Jean-François Giammari"
credits    = ["Baptiste Varamo","Jean-François Giammari"]
version    = "1.0"
"""

import io


def mots_Nlettres(lst_mot: list, n: int) -> list:
    """ Filter in a list the word who contain n letter
    list_mot -- List of words
    n -- Value limit
    return the filtered list
    """
    lst_filtered = []
    for e in lst_mot:
        if len(e) == n:
            lst_filtered.append(e)
    return lst_filtered


def commence_par(word: str, prefix: str) -> bool:
    """ Check if a word contain a specific prefix
    word -- The word to check
    prefix -- The prefix
    return True if the word contain the prefix
    """
    return word.startswith(prefix)


def finit_par(word: str, suffix: str) -> bool:
    """ Check if a word contain a specific suffix
    word -- The word to check
    suffix -- The suffix
    return True if the word contain the suffix
    """
    return word.endswith(suffix)


def finissent_par(lst_mot: list, suffix: str) -> list:
    """
    Filter in a list the word who contain a specific suffix
    list_mot -- List of words
    suffix -- The suffix
    return the filtered list
    """
    lst_filtered = []
    for e in lst_mot:
        if finit_par(e, suffix):
            lst_filtered.append(e)
    return lst_filtered


def commencent_par(lst_mot: list, prefix: str) -> list:
    """
    Filter in a list the word who contain a specific prefix
    list_mot -- List of words
    prefix -- The suffix
    return the filtered list
    """
    lst_filtered = []
    for e in lst_mot:
        if commence_par(e, prefix):
            lst_filtered.append(e)
    return lst_filtered


def liste_mots(lst_mot: list, prefix: str, suffix: str, n: int) -> list:
    """
    Filter in a list the word who contain a specific prefix
    list_mot -- List of words
    prefix -- The suffix
    return the filtered list
    """
    lst_Nfiltered = mots_Nlettres(lst_mot, n)
    lst_Pfiltered = commencent_par(lst_Nfiltered, prefix)
    lst_Sfiltered = finissent_par(lst_Pfiltered, suffix)
    return lst_Sfiltered


def dictionnaire(file: str) -> list:
    """
    Display content of a file.txt
    file -- Txt file to read
    return the list of word
    """
    print("Fichier " + file + " : ")
    with io.open(file, 'r', encoding='utf8') as f:
        dico = f.read().split('\n')

    return dico


def test_exercice2():
    """
    Test for exercice 2
    """
    lst_mot = ["jouer", "bonjour", "punir", "jour", "aurevoir", "revoir", "pouvoir", "cour", "abajour", "finir",
               "aimer"]
    print("Test mots_Nlettres [jour, cour] (4) : ", mots_Nlettres(lst_mot, 4))
    print("Test mots_Nlettres [aurevoir] (8) : ", mots_Nlettres(lst_mot, 8))
    print("Test if prefix jou : ", commence_par("jour", "jou"))
    print("Test if prefix er : ", commence_par("jour", "er"))
    print("Test if suffix our : ", finit_par("jour", "our"))
    print("Test if suffix rar : ", finit_par("jour", "rar"))
    print("Test if list suffix our : ", finissent_par(lst_mot, "our"))
    print("Test if list suffix er : ", finissent_par(lst_mot, "er"))
    print("Test if list prefix jou : ", commencent_par(lst_mot, "jou"))
    print("Test if list prefix p : ", commencent_par(lst_mot, "p"))
    print("Test liste mots (re, voir,6) [revoir]  : ", liste_mots(lst_mot, "re", "voir", 6))
    print("Test liste mots (jo, r,5) [jouer]  : ", liste_mots(lst_mot, "jo", "r", 5))
    #print(dictionnaire("littre.txt"))


test_exercice2()
