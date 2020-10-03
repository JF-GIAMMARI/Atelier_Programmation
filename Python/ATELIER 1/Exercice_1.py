#Auteur : Jean-François Giammari & Axel Frau
#Date : 07/09/2020 
#Version : 2
#Description : Calcule Salaire

""" Les inputs aurait pu être mis dans la fonction quitte à crée une fonction annexe dans ce seul but """

#EXERCICE 1


def calculer_salaire(nombre_heures:int,salaire_horaire:float )->float:
    """ 
    Cette fonction permet de calculer le salaire a partir du salaire horaire et du nombre d'heure de travail, en prenant en compte les majorations des heures supplémentaires
    (25% au-delà de 160h, 50% au-delà de 200h)
    """

    HEURE_PALIER = [160,200]
    MAJORATION_PALIER = 1.25
    salaire = nombre_heures*salaire_horaire 

    for i in range(len(HEURE_PALIER)): # Application des majorations
        if nombre_heures > HEURE_PALIER[i] :
            salaire += (nombre_heures-HEURE_PALIER[i]) * (salaire_horaire*MAJORATION_PALIER-salaire_horaire)
   
    return salaire
    

def test_unitaire(): # Fonction comparant le résultat obtenue et attendue dans les cas les plus significatif.
""" Pas de DocString """
    horaire_test = [0,10,0,10,159,165,200,210]
    salaire_test = [0,0,10,10,10,10,10,10]
    resultat_test= [0,0,0,100,1590,1662.5,2100,2250]

    for i in range(0,len(horaire_test)) :
        if calculer_salaire(horaire_test[i],salaire_test[i]) == resultat_test[i] :
            print(">",end="")
        else :
            print("X",end="")
    

#Appel des fonctions
test_unitaire()
nombre_heures = int(input("\nVotre nombre d'heure :"))
salaire_horaire = int(input("Votre salaire horaire :"))
print("Votre salaire sera : {} € ".format(calculer_salaire(nombre_heures,salaire_horaire )))
