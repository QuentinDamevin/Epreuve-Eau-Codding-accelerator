#Creez un programme qui affiche ses arguments reçus a l'envers 
import sys

arguments = sys.argv
#condition si un arguments minimum n'est pas passé on sort du programme
if len(arguments) < 2:
    print("Erreur")
    exit()
#solution
else:
    arguments_multiple = arguments[::-1]
    for arg in arguments_multiple:
        print(arg)