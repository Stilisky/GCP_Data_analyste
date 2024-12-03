#!/usr/bin/python3

myList = [23, 'jgj fdj', "holo", 54, "frero", 'mieux']
# Affichage 1
i=0
while(i < len(myList)): 
    print(myList[i])
    i += 1

# Affichage 2
for index, val in enumerate(myList):
    print(val)

# Quizz 2
months  = [
    "Janvier",
    "Février",
    "Mars",
    "Avril",
    "Mai",
    "Juin",
    "Juillet",
    "Août",
    "Septembre",
    "Octobre",
    "Novembre",
    "Décembre"
]

days_per_month = [
    31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
]

list =[]
for (index, val) in enumerate(months):
    list.append(val)
    list.append(days_per_month[index])

print(list)

