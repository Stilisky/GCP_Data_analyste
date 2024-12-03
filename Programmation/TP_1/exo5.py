#!/usr/bin/python3

#abcdefgmhijklmnopqrstuvwxyz
alpha_principal = "abcdefghijklmnopqrstuvwxyz"
crypte_alpha = ''
message = input("Entrer le message: ")
msg_crypt = ''
clef = int(input("Entrer la clef: "))
for letter in alpha_principal:
    position = alpha_principal.find(letter)
    if((position + clef + 1)  < 27):
        crypte_alpha +=  alpha_principal[position:(position +1)]
    else :
        sous = 26 - (position + clef + 1) 
        crypte_alpha += alpha_principal[sous: (sous+1)]

for val in message:
    pos = alpha_principal.find(val)
    if(pos != -1) :
        msg_crypt += crypte_alpha[pos]
    else:
        msg_crypt += val

print(alpha_principal)
print(crypte_alpha)
print ("Message chiffre: ", msg_crypt)

