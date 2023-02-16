#Créez un programme qui affiche toutes les valeurs comprises entre deux nombres dans l’ordre croissant. Min inclus, max exclus.
import sys
arguments= sys.argv



def gestion_erreurs():
    if len(arguments) < 3:
        return True
    if not arguments[1].isnumeric() or not arguments[2].isnumeric():
        return True
    if arguments[1] >= arguments[2]:
        return True
    return False   

#Boucle + affichage
if gestion_erreurs() == False:
    min_arg = int(arguments[1])
    max_arg = int(arguments[2])
    for x in range(min_arg,max_arg):
        print(x,end=' ')
else:
    print("Erreur")


