#Créez un programme qui affiche la différence minimum absolue entre deux éléments d’un tableau constitué uniquement de nombres. Nombres négatifs acceptés.
import math
import os
import random
import re
import sys 
arguments = sys.argv
from math import inf
#Fonction qui retourne que des nombre
def only_numbers(tab):
    for x in tab:
        if not x.isdigit():
            return False
    return True

def dif_min(tab):
    minimum_absolute = inf
    for x in range(len(tab)):
        for y in range(x+1,len(tab)):
            calcul = abs(tab[x]-tab[y])
            if calcul < minimum_absolute:
                minimum_absolute = calcul
    return minimum_absolute

tableaux = arguments[1:]
if only_numbers(tableaux)==True and len(arguments) >= 3:
    tableux_int = list(map(int, tableaux))
    print(dif_min(tableux_int))
else:
    print("Veuillez rentrer deux arguments contenant que des chiffres")
