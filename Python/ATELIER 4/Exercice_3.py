"""
Exercice 3 de l'atelier 4 : Jeu du pendu
file       = "Exercice_3.py"
author     = "Baptiste Varamo & Jean-François Giammari"
credits    = ["Baptiste Varamo","Jean-François Giammari"]
version    = "1.0"
"""

import random
import io


def placesLettre(char: str, mot: str) -> list:
    """ Check if a letter is in a word
       char -- The letter
       mot -- The word
       return the list with index
       """
    char = char[0]
    if not char in mot:
        return []
    else:
        res = []
        for i in range(0, len(mot)):
            if mot[i] == char:
                res.append(i)
        return res


def outputStr(mot: str):
    """
    Transforme textthe mystery text
    mot -- The word
    return a str of "_"
    """
    str = ""
    for i in mot:
        str += '_'
    return str


def runGame():
    """ Launch the game """
    with io.open("littre.txt", 'r', encoding='utf8') as f:
        dico = f.read().split('\n')

    word = random.randint(0, len(dico))
    word = dico[word]
    game_str = outputStr(word)

    i = 0
    while i <= 5:
        if not '_' in game_str:
            print("Vous avez gagné !")
            return 1

        print("Nombre de coup restant : ", 5 - i)
        print(game_str)
        char = input('Saisir une lettre : ')[0]

        pos = placesLettre(char, word)
        if pos:
            for j in range(0, len(pos)):
                game_str = game_str[:pos[j]] + char + game_str[pos[j] + 1:]
        else:
            i += 1
            print("LOUPé")
    print("Vous avez perdu.. Le mot était " + word)


runGame()
