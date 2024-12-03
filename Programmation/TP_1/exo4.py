#!/usr/bin/python3

chaine = input("Entrer la chaine: ")
chaine_len = 0
for _ in chaine:
    chaine_len += 1

print("La longueur de la chaine est: ", chaine_len, "\nTest de la fonction len: ", len(chaine))