#!/usr/bin/python3

list_of_list = []
dimension = int(input("Entrer la dimension de votre triangle: "))

while(dimension <0):
    dimension = int(input("Entrer la dimension de votre triangle: "))


for i in range(dimension):
    a_list = []
    for j in range(dimension):
        a_list.append(0)
    list_of_list.append(a_list)


for i in range(dimension):
    sous_list = list_of_list[i]
    for j in range (len(sous_list)):
        print(sous_list[j], end=" ")
    print()
    
        