#!/usr/bin/python3

repeat = True
myList = []

while repeat:
    number = int(input("Entrer un nombre: "))
    if (number == 0):
        repeat = False
    elif number not in myList:
        myList.append(number)
        myList.sort()

for (index, value) in enumerate(myList):
    print(value)

