#Creez un programme qui determine si une chaine de caractere ne contient que des chiffres.

import sys

arguments = sys.argv

#Gestion erreur (si il n'y a aucun argument de rentré)
if len(arguments) < 2:
    print("Veuillez rentrer un argument")
    exit()
if len(arguments) > 2:
    print("Veuillez rentrer 1 seul arguments")
    exit()
try:
    #on convertie en int si  impossible alors il y a des lettres.
    arguments_1_int = int(arguments[1])
    print(True)
except:
    print(False)

