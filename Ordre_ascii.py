#Créez un programme qui trie les éléments donnés en argument par ordre ASCII.
import sys

arguments =  sys.argv

tableau = arguments[1:]
#Fonction verification si il n'y a que des lettres
def only_letters(tableaux):
    for x in tableaux:
        if not x.isalpha():
            return False
    return True
#Fonction mettre en ordre ascii
def ordre_ascii(tab):
    for x in range(0,len(tab)):
        index = x 
        for y in range(x+1,len(tab)):
            if tab[y] < tab[index]:
                index = y
        tab[index],tab[x] = tab[x],tab[index]
    return tab

#Affichage 
if only_letters(tableau) == True and len(arguments) >=2:
    tableau_trié = ordre_ascii(tableau)
    for x in tableau_trié:
        print(x,end=" ")
    print()
else:
    print("Un argument minumum qui ne contient que des lettres.")



#if only_letters(tab) == True and len(arguments) >=2:
   