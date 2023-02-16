import sys

arguments = sys.argv

if len(arguments) != 2:
    print("Un argument est requis")
    exit()

if not arguments[1].isalpha():
    print("error")
    exit()

arguments_1 = arguments[1]
#ici on parcours combien de lettre il ya 
arg = []
x=0
for x in range(len(arguments_1)):
    if x%2 == 0:
        arg.append(arguments_1[x].lower())
        
    else:
        arg.append(arguments_1[x].upper())
      

print("".join(arg))