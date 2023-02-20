import sys 
arguments = sys.argv
#Fonction pour le tri a bulle
def tri_a_bulle(tab):
    for i in range(len(tab)-1,0,-1):
        index = i 
        for y in range(0,i):
            if tab[index] < tab[y]:
                index = y
        tab[i],tab[index] = tab[index],tab[i]
    return tab
#Fonction qui verifie si il y a que des chiffres dans un tableaux
def only_chiffres(tableau):
    for element in tableau:
        if not element.isdigit():
            return False
    return True


tableaux = arguments[1:]
#Affichage
if only_chiffres(tableaux) == True and len(arguments) >= 3:
    print(tri_a_bulle(tableaux))
else:
    print("Vous devez rentrer deux arguments qui ne contiennent que des chiffres.")