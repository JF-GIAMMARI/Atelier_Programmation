#Auteur : Jean-François Giammari & Axel Frau
#Date : 07/09/2020 
#Version : 1
#Description : Reprographie

#EXERCICE 4

def photocopie_price(nbr_photocopie:int)->float:
    """
    Cette exercice permet de calculer rapidement le prix d'impression de photocopie en fonction du nombre de photocopie et des réductions associé
    -> 10 première photocopie a 0.10€
    -> 20 suivantes a 0.09€
    -> autres a 0.08€
    """
    
    PALIER_PRIX=[10,30] 
    PRIX_1=0.1 
    PRIX_2=0.09
    PRIX_3=0.08 
    PRIX_10=1 
    PRIX_20=1.8 
   
    if nbr_photocopie <= PALIER_PRIX[0] :  #Application prix 1
        res = nbr_photocopie*PRIX_1
    elif nbr_photocopie<=PALIER_PRIX[1] : #Application prix 2
        res = PRIX_10+(nbr_photocopie-PALIER_PRIX[0])*PRIX_2
    else: #Application prix 3
        res = PRIX_10+PRIX_20+(nbr_photocopie-PALIER_PRIX[1])*PRIX_3
  
    return round(res,2)

def test_unitaire(): # Fonction comparant le résultat obtenue et attendue dans les cas les plus significatif.

    nbr_photoco_test = [0,10, 30, 667, 45, 27]
    nbr_photoco_res = [0.0, 1.0, 2.8, 53.76, 4.0, 2.53]

    for i in range (0, len(nbr_photoco_test)) :  
        if photocopie_price(nbr_photoco_test[i]) == nbr_photoco_res[i]:
            print(">",end="")
        else : 
            print("X",end="")
        
    

#Appel des fonctions
test_unitaire()
nbr_photocopie = int(input('\nCombien de photocopie voulez vous ? '))
print("Le prix total pour", nbr_photocopie, "photocopie(s) est de " + str(photocopie_price(nbr_photocopie)) + "€")
