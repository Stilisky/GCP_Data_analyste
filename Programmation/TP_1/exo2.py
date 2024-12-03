#!/usr/bin/python3

# Verifions si une année est bissextile
annee = input("Entrer une annee: ")

val_an = int(annee)

if (val_an % 400 == 0 or ((val_an % 4 == 0) and (val_an % 100 != 0))) :
    print("L'annee ", annee, " est bissextile")
else :
    print("L'annee ",annee," n'est pas bissextile")