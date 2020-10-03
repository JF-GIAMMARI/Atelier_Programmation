# Auteur : Jean-François Giammari & Axel Frau
# Date : 08/09/2020
#Version : 1
# Description : Calcul d'IMC

# EXERCICE 1

def message_imc(imc: float) -> str:
    """ 
    Cette fonction permet d'interpréter l'état de santé d'une personne en fonction de son IMC
    """

    #Definition des constantes de valeur IMC : 
    IMC_VALUE_MAIGREUR = 16.5
    IMC_VALUE_NORMAL = 18.5
    IMC_VALUE_SURPOIDS = 25
    IMC_VALUE_OBESITE_MODERE = 30
    IMC_VALUE_OBESITE_SEVERE = 35
    IMC_VALUE_OBESITE_MORBIDE = 40

    #Test pour determiner dans quelle catégorie ce trouve lIMC donner en paramètre : 
    message = "dénutrition ou famine"
    if imc > IMC_VALUE_MAIGREUR:
        message = "maigreur"
    if imc > IMC_VALUE_NORMAL:
        message = "corpulence normale"
    if imc > IMC_VALUE_SURPOIDS:
        message = "surpoids"
    if imc > IMC_VALUE_OBESITE_MODERE:
        message = "obésité modérée"
    if imc > IMC_VALUE_OBESITE_SEVERE:
        message = "obésité sévère"
    if imc > IMC_VALUE_OBESITE_MORBIDE:
        message = "obésité morbide"

    return message


def test_unitaire(): # Fonction comparant le résultat obtenue et attendue dans les cas les plus significatif.

    imc_test = [16, 17, 19, 26, 31, 36, 45]
    resultat_test = ["dénutrition ou famine", "maigreur", "corpulence normale",
                     "surpoids", "obésité modérée", "obésité sévère", "obésité morbide"]

    for i in range(0, len(imc_test)):
        if message_imc(imc_test[i]) == resultat_test[i]:
            print(">", end="")
        else:
            print("X", end="")


#Appel des fonctions
test_unitaire()
print("\nActuellement vous êtes diagnostiquer avec un état de ",
message_imc(float(input("Entrer votre IMC : "))))
