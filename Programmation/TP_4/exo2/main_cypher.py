import cryptoutils
import string

# message = input("Entrer un message: ")
# clef = int(input("Entrer votre clef: "))
# is_valid = True
# decrypt = False
# while(is_valid):
#     text = int(input('Voulez-vous faire du cryptage ? (1- oui ou 2- non): '))

#     if(text == 1):
#         is_valid = False
#     elif (text == 2):
#         decrypt = True
#         is_valid = False
#     else:
#         print("Erreur! Reprenez svp!")

# print("Votre resultat: ", cryptoutils.cesar_cypher(message, clef, decrypt))

message = input("Entrer un message: ")
clef = input("Entrer votre mot-clef: ")
alphabet = string.ascii_lowercase
is_valid = True
decrypt = False
while(is_valid):
    text = int(input('Voulez-vous faire du cryptage ? (1- oui ou 2- non): '))

    if(text == 1):
        is_valid = False
    elif (text == 2):
        decrypt = True
        is_valid = False
    else:
        print("Erreur! Reprenez svp!")

result=''
for i in range(len(message)):
    lo = i%len(clef)
    position = alphabet.find(clef[lo])
    result += cryptoutils.cesar_cypher(message[i], position, decrypt)

print("Votre resultat: ", result)
