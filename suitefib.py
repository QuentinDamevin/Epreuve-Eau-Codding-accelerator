import sys
arguments = sys.argv
#Gestion erreurs
def gestion_erreur():
    if  len(arguments) != 2:
        return True
    if not arguments[1].isnumeric():
        return True
    if arguments[1] < 0:
        return True
    return False 

num1,num2=[0,1]
fibonnaci_list = []
for x in range(10):
    fibonnaci_list.append(num1)
    calcul = num1+num2
    num1 = num2
    num2 = calcul

#Affichage
if gestion_erreur() == False:
    index = fibonnaci_list.index(int(arguments[1]))
    print(index)
else:
    print("Veuillez rentrer un seul nombre positif")