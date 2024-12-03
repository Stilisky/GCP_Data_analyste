#!/usr/bin/python3

chaine = input("Entrer une chaine: ")
chaine_length = len(chaine)
second_chaine = chaine
e_occurence = 0
while(chaine_length > 0) :
    letter = second_chaine[0:1]
    print(letter)
    if (letter == 'e'):
        e_occurence += 1
    second_chaine = second_chaine[1:]
    chaine_length -=1


print('Nous avons ', e_occurence, 'caractere(s) de e.')
