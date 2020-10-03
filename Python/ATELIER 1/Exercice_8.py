# Auteur : Jean-François Giammari & Axel Frau
# Date : 08/09/2020
#Version : 1
# Description : Compagnie d'assurance automobile

# EXERCICE 8

def tarification(age="", annee_permis="", nbr_accidents="", annee_assure="")-> str:
    """ 
    Cette fonction permet de definir la famille d'assurance que peut obtenir un client en fonction de sont age, du nombre d'année de permis, 
    du nombre d'accidents, et du nombre d'année assuré dans cette assurance
    """

    if age == "": # Si aucun paramètre n'est définis, on demande une entrer utilisateur
        while age.isdigit() == False:
            age = input("Veuillez saisir votre age : ")
        while annee_permis.isdigit() == False:
            annee_permis = input("Veuillez saisir le nombre d'année ou vous avez été titulaire de votre permis : ")
        while nbr_accidents.isdigit() == False:
            nbr_accidents = input("Veuillez saisir votre nombre d'accident: ")
        while annee_assure.isdigit() == False:
            annee_assure = input("Veuillez saisir votre nombre d'année assurer chez nous : ")

    AGE_PIVOT = 25
    PERMIS_PIVOT = 2
    ASSURANCE_BONUS = 1

    tarif_name = ["Refuser", "Bleu", "Vert", "Orange", "Rouge"]
    tarif = 4 # Par défaut le tarif est Rouge

    # Conversion en entier des entrées/paramètres
    age = int(age)
    annee_permis = int(annee_permis)
    nbr_accidents = int(nbr_accidents)
    annee_assure = int(annee_assure)


    if age < AGE_PIVOT: 
        if nbr_accidents > 0:
            tarif = 0
        else:
            if annee_permis > PERMIS_PIVOT:
                tarif = 3
    else:
        if annee_permis > PERMIS_PIVOT:
            if nbr_accidents == 0:
                tarif = 2
            elif nbr_accidents ==1:
                tarif = 3
            elif nbr_accidents > 2:
                tarif = 0
        else:
            if nbr_accidents == 0:
                tarif = 3

    if tarif >=2 and annee_assure > ASSURANCE_BONUS  : 
            tarif -=1
 
    return tarif_name[tarif] 




# test_unitaire() lance une série de tests comparant le résultat obtenue et attendue dans les cas les plus significatif.
def test_unitaire():
    age_test = [20, 20, 20,20, 26, 30, 32, 34, 35,26]
    accidents_test= [1,0,0,0,1, 0, 1, 2, 6,0]
    apermis_test = [1,1,4,4,1,3,4,5,6,1]
    aassure_test= [0,2,0,3,0,0,0,2,3,2]
    resultat_test = ["Refuser","Orange", "Orange", "Vert", "Rouge", "Vert","Orange","Orange","Refuser","Vert"]
    succes = True

    for i in range(0,len(age_test)) :
        if tarification(age_test[i], apermis_test[i], accidents_test[i], aassure_test[i]) == resultat_test[i] :
            print(">",end="")
        else :
            print("X",end="")
            succes = False

    if succes == True :
        print(" TEST IS SUCCES")
    else :
        print(" TEST IS FAILED")




test_unitaire()
print("Vous êtes {}".format(tarification()))