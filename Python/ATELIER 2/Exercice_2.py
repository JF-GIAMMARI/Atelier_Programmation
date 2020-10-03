#Auteur : Jean-François Giammari & Axel Frau
#Date : 08/09/2020 
#Version : 2
#Description : Année Bissextile

#EXERCICE 2
"""
Cette fonction nous permet de savoir si une année est bisextile ou non.
Si l'année est divisible par 4 et pas par 100 ou bien qu'elle est divisible par 400 alors l'expression renvoi True signifiant que l'année est bissextile
"""

def est_bissextile(year:int) -> bool:
    #On return directement une expression boolèenne qui verifie que l'année donnnée en paramètre est une année bissextile
    return (((year%4 == 0) and not (year%100 == 0) ) or (year%400 == 0))


def test_unitaire(): # Fonction comparant le résultat obtenue et attendue dans les cas les plus significatif.

    year_test = [2012, 2013, 2000,400]
    year_res = [True, False, True, True]

    for i in range(0,len(year_test)) :
        if est_bissextile(year_test[i]) == year_res[i] :
            print(">",end="")
        else :
            print("X",end="")


#Appel des fonctions
test_unitaire()
