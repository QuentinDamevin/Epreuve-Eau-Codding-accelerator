"""Créez un programme qui affiche le premier index d’un élément recherché dans un tableau. Le tableau est constitué de tous les arguments sauf le dernier. L’élément recherché est le dernier argument. Afficher -1 si l’élément n’est pas trouvé."""

import sys
arguments = sys.argv
#Gestion erreurs
if not len(arguments) > 2:
    print("erreur")
    exit()

#Variable
liste_arg = arguments[1:-1]
dernier_arg = arguments[-1]

#Boucle+affichage
for x in range(len(liste_arg)):
    if liste_arg[x] == dernier_arg:
        print(x)
        break
else:
    print("-1")