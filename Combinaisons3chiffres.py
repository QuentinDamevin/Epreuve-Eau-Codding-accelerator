#Créez un programme qui affiche toutes les différentes combinaisons possibles de trois chiffres dans l’ordre croissant, dans l’ordre croissant. La répétition est volontaire.
print("Début du programme qui affiche toutes les différentes combinaisons possibles de trois chiffres dans l’ordre croissant")
for i in range(10):
    for j in range(i+1, 10):
        for k in range(j+1, 10):
            print(i, j, k)
print("Fin du programme")