#!/usr/bin/python3
import math

# Fontion pour dire hello

def say_hello():
    print("Bonjour")

for _ in range(5):
    say_hello()
print('----------------------------------------')
# Function pour calculer le cube d'un arg
def cube(nombre):
    return math.pow(nombre, 3)

print("cube de 2: ", cube(2))

print('----------------------------------------')
def cube_of_cube(value):
    return cube(cube(value))

print("Cube du cube de 2: ", cube_of_cube(2))