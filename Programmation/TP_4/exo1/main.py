import calcul

def isDigitNumber():
    isEnable = True
    while(isEnable):
        nombre = input("Entrer un entier: ")
        if (nombre.isdigit()):
            isEnable = False
            return int(nombre)
        
print("---Nombre 1---------")
nombre1 = isDigitNumber()
print("---Nombre 2---------")
nombre2 = isDigitNumber()

print("Addition")
# print(nombre1 + " + " + nombre2 +' = '+ calcul.addition(nombre1, nombre2))
print(calcul.addition(nombre1, nombre2))

print("Soustraction")
print(calcul.soustraction(nombre1, nombre2))
# print(nombre1 + " + " + nombre2 +' = '+ calcul.soustraction(nombre1, nombre2))

print("Multiplication")
print(calcul.multiplication(nombre1, nombre2))
# print(nombre1 + " x " + nombre2 +' = '+ calcul.multiplication(nombre1, nombre2))

print("Division")
if(nombre2 != 0):
    print(calcul.division(nombre1, nombre2))
    # print(nombre1 + " / " + nombre2 +' = '+ calcul.division(nombre1, nombre2))
else:
    print("Une division par 0 n'est pas possible!")
