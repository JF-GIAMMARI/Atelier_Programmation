#Auteur : Jean-François Giammari & Axel Frau
#Date : 08/09/2020 
#Version : 1
#Description : Elections législatives

#EXERCICE 7

def exercice_7(resultats:list)->str:
    """
    Cette fonction permet de calculer les resultat des élections pour le premier candidat
     de la liste passée en paramètre.
    """
    TAUX_MIN_SECOND_TOUR = 0.125
    LONGUEUR_DE_LISTE = len(resultats)
    total_de_votes = 0
    #calcul du nombre total de votes
    for i in range(0, LONGUEUR_DE_LISTE):
        total_de_votes += resultats[i]
    if resultats[0] >= total_de_votes/2 :
        return "win"
    for i in range(1, LONGUEUR_DE_LISTE):
        if resultats[i] >= total_de_votes/2 :
            return "éliminé_majorité"
    if resultats[0] >= total_de_votes * TAUX_MIN_SECOND_TOUR  :
        return "second_tour"
    else :
        return "eliminé_under_12.5%"

        

def test_unitaire():
    votes_test = [[160,46,31,42], [10,56,76,9],[100,65,89,76], [10,43,95,60]]
    res = ["win", "éliminé_majorité", "second_tour","eliminé_under_12.5%"]
    success = True
    for i in range (0, len(votes_test)) :
        if exercice_7(votes_test[i]) == res[i]:
            print(">",end="")
        else : 
            print("X",end="")
            success = False
    
    if success == True :
        print(" TEST IS SUCCESSFUL")
    else :
        print(" TEST FAILED")

test_unitaire()
VOTE_C1 = int(input("Entrez les resultat du candidat 1 : "))
VOTE_C2 = int(input("Entrez les resultat du candidat 2 : "))
VOTE_C3 = int(input("Entrez les resultat du candidat 3 : "))
VOTE_C4 = int(input("Entrez les resultat du candidat 4 : "))
res = exercice_7([VOTE_C1,VOTE_C2,VOTE_C3,VOTE_C4])
if res == "win": 
    print("Le candidat 1 a gagné à la majorité ! Félicitation !")
elif res == "éliminé_majorité" : 
    print("Un candidat a obtenue la majorité, le candidat 1 a perdue")
elif res == "second_tour" : 
    print("Le candidat numéro 1 passe au second tour")
else : 
    print("Le candidat 1 n'a pas eu assez de voies pour passer au second tour")