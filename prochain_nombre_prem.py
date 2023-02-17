import sys

def list_premier(n):
    primes = []
    for num in range(2, n+1):
        is_prime = True 
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break 
        if is_prime:
            primes.append(num)
    return primes

arguments = sys.argv
#Gestion erreurs
if len(arguments) !=2:
    print("Veuillez rentrer un seul argument")
    exit()
if not arguments[1].isnumeric():
    print("Veuillez rentrer un chiffre")
    exit()

primes = list_premier(1000)
arguments_int = int(arguments[1])
#On boucle pour trouver le nombre premier suivant.
for x in range(len(primes)):
    if primes[x] == arguments_int:
        print(primes[x+1])
        break
else:
    print("Erreur ce n'est pas un nombre premier")
