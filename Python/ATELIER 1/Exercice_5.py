#Auteur : Jean-François Giammari & Axel Frau
#Date : 08/09/2020 
#Version : 1
#Description : Calcul de frais portuaires

# EXERCICE 5

def frais_portuaire(nom:str,longueur:int, categorie:int)->list:
    """ 
    Cette fonction permet de calculer les frais portuaire annuel d'une place dans un port 
    en fonction de la longueur et de la catégorie du bateau en question.
    """
    
    # Definissions des tailles possible
    PETIT_BATEAU = 5
    MOYEN_BATEAU = 10
    GRAND_BATEAU = 12

    # Definissions des prix par défaut
    cout_mensuel = 100
    taxe_annuel = 100

    # Vérification de la taille
    if longueur >= PETIT_BATEAU :
        cout_mensuel = 200
    if longueur > MOYEN_BATEAU :
        cout_mensuel = 400
    if longueur > GRAND_BATEAU :
        cout_mensuel = 600

    #Vérification de la catégorie
    if categorie == 2 :
        taxe_annuel = 150
    elif categorie == 3 :
        taxe_annuel = 250


    frais = cout_mensuel*12+taxe_annuel #Division par mois

    return [nom,frais]

def test_unitaire(): # Fonction comparant le résultat obtenue et attendue dans les cas les plus significatif.

    longueur_test = [4, 5, 11, 15]
    categorie_test = [1,2,3,1]
    resultat_test= [1300,2550,5050,7300]

    for i in range(0,len(longueur_test)) :
        if frais_portuaire("Default" ,longueur_test[i], categorie_test[i])[1] == resultat_test[i] :
            print(">",end="")
        else :
            print("X",end="")


#Appel des fonctions
test_unitaire()

nom = input("\nVeuillez saisir le nom de votre bateau : ")
longueur = float(input("Veuillez saisir la longueur de votre bateau en m :  "))
categorie = int(input("Veuillez saisir la catégorie de votre bateau (1,2,3) : "))
result = frais_portuaire(nom,longueur,categorie)
print("Le coût annuel d'une place au port pour le voilier {} est de {} euros".format(result[0], result[1]))
