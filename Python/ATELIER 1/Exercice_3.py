#Auteur : Jean-François Giammari & Axel Frau
#Date : 07/09/2020 
#Version : 1
#Description : Impôts

#EXERCICE 3


def imposable(sexe:str, age:int)->str:
    """ 
    Cette fonction permet de savoir en fonction de l'age et du sexe d'un habitant si il est imposable ou non
    -> Homme de plus de 20ans -> Imposable
    -> Femme entre 18 et 35 ans -> Imposable
    -> Autre -> Non Imposable
    """
    
    AGE_HOMME_LIMITE = 20 
    AGE_HOMME_MIN = 18
    AGE_HOMME_MAX = 35
    result = "Vous n'êtes pas imposable"

    # Application des conditions pour vérifier l'imposabilité
    if sexe == "H" and age > AGE_HOMME_LIMITE or sexe == "F" and age >= AGE_HOMME_MIN and age <= AGE_HOMME_MAX :
        result = "Vous êtes imposable"

    return result

def test_unitaire(): # Fonction comparant le résultat obtenue et attendue dans les cas les plus significatif.
    sexe_test = ["H","F","F","F","H"]
    age_test = [20,17,36,19,21]
    resultat_test= ["Vous n'êtes pas imposable","Vous n'êtes pas imposable","Vous n'êtes pas imposable","Vous êtes imposable","Vous êtes imposable"]

    for i in range(0,len(sexe_test)) :
        if imposable(sexe_test[i],age_test[i]) == resultat_test[i] :
            print(">",end="")
        else :
            print("X",end="")



#Appel des fonctions
test_unitaire()
sexe = input("\nVotre sexe (H/F) :")
age = int(input("Votre age: "))
print("Votre salaire sera : {} € ".format(imposable(sexe, age)))

