#!/usr/bin/python3

EcoleName = "Seme-City"

# Extraction de Seme et city de la chaine
stringA = EcoleName[0:4]

stringB= EcoleName[5:]

print("1- Extraction des chaine:\n\t1- Chaine 1: ", stringA,"\n\t2- Chaine 2: ", stringB)

print("--------------------------------------------------------")
rec = stringA + '-' + stringB
print("2- Reconstitution de la chaine: ", rec)
