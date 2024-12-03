#!/usr/bin/python3

#Redefine key
def get_key(key):
    if(new_key<=0 and new_key>=26):
        return new_key
    else:
        val = key % 26
        return val

#abcdefgmhijklmnopqrstuvwxyz
alpha_principal = "abcdefghijklmnopqrstuvwxyz"
crypte_alpha = ''
message = input("Entrer le message: ")
msg_crypt = ''
new_key = int(input("Entrer la clef: "))
#Get new key
clef = get_key(new_key)

for letter in alpha_principal:
    position = alpha_principal.find(letter)
    if((position + clef + 1)  < 27):
        crypte_alpha +=  alpha_principal[(position + clef):(position + clef +1)]
    else :
        val = position + clef +1
        sous = val - 26 
        crypte_alpha += alpha_principal[sous: (sous+1)]
    # print("letter: ", letter, " posi: ", position, "Crypte: ",crypte_alpha)

for val in message:
    pos = alpha_principal.find(val)
    if(pos != -1) :
        msg_crypt += crypte_alpha[pos]
    else:
        msg_crypt += val

# print()
# print(alpha_principal)
# print(crypte_alpha)
print ("Message chiffre: ", msg_crypt)

