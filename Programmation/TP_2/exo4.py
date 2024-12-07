#!/usr/bin/python3

import numpy as np

dimension = int(input("Entrer la dimension de votre triangle: "))

while(dimension <0):
    dimension = int(input("Entrer la dimension de votre triangle: "))

list_of_list = np.zeros((dimension, dimension), dtype=int)

for i in range(dimension):
    if(i == 0):
        list_of_list[i][i] = 1
    else:
        for j in range(dimension):
            if (j ==0) :
                list_of_list[i][j] = list_of_list[i-1][j]
            else:
                list_of_list[i][j] = list_of_list[i-1][j] + list_of_list[i-1][j-1]

for i in range(dimension):
    tab = list_of_list[i]
    for j in range(dimension):
        if(tab[j] != 0):
            print(tab[j], end=' ')
    print()



                

























# for i in range(dimension):
#     a_list = []
#     for j in range(dimension):
#         a_list.append(0)
#     list_of_list.append(a_list)


# for i in range(dimension):
#     sous_list = list_of_list[i]
#     for j in range (len(sous_list)):
#         print(sous_list[j], end=" ")
#     print()
    
