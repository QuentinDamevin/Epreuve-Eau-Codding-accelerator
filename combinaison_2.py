#Créez un programme qui affiche toutes les différentes combinaisons de deux nombre entre 00 et 99 dans l’ordre croissant.
#Solution
print("Début du programme qui affiche toutes les différentes combinaisons de deux nombre entre 00 et 99 dans l’ordre croissant.")
for x in range(10):
        for y in range(0,10):
            for w in range(0,10):
                for d in range(y+1,10):
                    print(x,y,w,d,end=" , ") 
print("Fin du programme")
    

