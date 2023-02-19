#Creez un programme qui détermine si une chaine de caracteres se trouve dans une autre.
import sys

arguments = sys.argv


def recherche_chaine(chaine, sous_chaine):
    if sous_chaine in chaine:
        return True
    else:
        return False

#Gestion erreurs
if len(arguments) != 3:
    print("erreur deux arguments sont necessaires.")
    exit()

#Initialisation variable + appel fonction.
arguments_1 = arguments[1]
arguments_2 = arguments[2]
if recherche_chaine(arguments_1,arguments_2) == True:
    print("True")
else:
    print("False")
