#Créez un programme qui trie une liste de nombres. Votre programme devra implémenter l’algorithme du tri par sélection.

import sys
arguments = sys.argv
#Fonction
def trie_liste(array):
    for x in range(len(array)):
        index = x
        for y in range(x+1,len(array)):
            if array[y] < array[index]:
                index = y
        array[x],array[index] = array[index],array[x]
    return array
#Fonction pour verifier si il n'y a que des chiffres 
def only_chiffres(tableau):
    for element in tableau:
        if not element.isdigit():
            return False
    return True

tableaux = arguments[1:]
#Affichage
if only_chiffres(tableaux) == True and len(arguments) >= 3:
    print(trie_liste(tableaux))

else:
    print("Vous devez rentrer deux arguments qui ne contiennent que des chiffres.")
