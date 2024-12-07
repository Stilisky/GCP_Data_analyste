#!/usr/bin/python3

import string

#Redefine key
def get_key(key):
    if(key<=0 and key>=26):
        return key
    else:
        val = key % 26
        return val

def cesar_crypyt(alpha_principal, message, new_key) :
    crypte_alpha = ''
    msg_crypt = ''
    clef = get_key(new_key)

    for letter in alpha_principal:
        position = alpha_principal.find(letter)
        if((position + clef + 1)  < 27):
            crypte_alpha +=  alpha_principal[(position + clef):(position + clef +1)]
        else :
            val = position + clef +1
            sous = val - 26 
            crypte_alpha += alpha_principal[sous: (sous+1)]

    for val in message:
        pos = alpha_principal.find(val)
        if(pos != -1) :
            msg_crypt += crypte_alpha[pos]
        else:
            msg_crypt += val

    return msg_crypt

def cesar_decrypyt(alpha_principal, message, new_key) :
    crypte_alpha = ''
    msg_decrypt = ''
    clef = get_key(new_key)

    for letter in alpha_principal:
        position = alpha_principal.find(letter)
        if((position + clef + 1)  < 27):
            crypte_alpha +=  alpha_principal[(position + clef):(position + clef +1)]
        else :
            val = position + clef +1
            sous = val - 26 
            crypte_alpha += alpha_principal[sous: (sous+1)]

    for val in message:
        pos = crypte_alpha.find(val)
        if(pos != -1) :
            msg_decrypt += alpha_principal[pos]
        else:
            msg_decrypt += val

    return msg_decrypt

def is_letter(letter):
    minuscule = string.ascii_lowercase
    majuscule = string.ascii_uppercase

    if((minuscule.find(letter) != -1) or (majuscule.find(letter) != -1)):
        return True
    else:
        return False
    

def cesar_cypher(msg, clef, decrypt=False):
    # print(decrypt)
    if decrypt:
        msg_decrypt = ''
        for letter in msg:
            is_valid = is_letter(letter)
            if is_valid :

                asc_number = ord(letter)
                alph = ''

                if (asc_number >= 65 and asc_number <= 90 ):
                    alph += string.ascii_uppercase
                else :
                    alph += string.ascii_lowercase
                
                msg_decrypt += cesar_decrypyt(alph, letter, clef)
            else:
                msg_decrypt += letter
        return msg_decrypt
    else:
        msg_crypt = ''
        for letter in msg:
            is_valid = is_letter(letter)
            if is_valid :

                asc_number = ord(letter)
                alph = ''

                if (asc_number >= 65 and asc_number <= 90 ):
                    alph += string.ascii_uppercase
                else :
                    alph += string.ascii_lowercase
                msg_crypt += cesar_crypyt(alph, letter, clef)
            else:
                msg_crypt += letter
        return msg_crypt


