import sys

arguments = sys.argv
#Gestion erreurs
if len(arguments) < 2:
    print("Veuillez rentrer un argument")
    exit()
if arguments[1].isnumeric():
    print("Erreur veuillez rentrer que des lettres")
    exit()


#On passe l'arguments en miniscule pour la casse
arguments_1 = arguments[1].lower()
#Split afin de crée une liste 
list_chaine = arguments_1.split()
#Parcours de la liste puis affectation de la premiere lettre de chaque elements en majuscule 
for x in range(len(list_chaine)):
    mot = list_chaine[x]
    lettre = mot[0].upper() + mot[1:]
    print(lettre , end=" ")
print()