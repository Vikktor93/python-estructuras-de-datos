"""Reto 1: crear una arreglo y ordenarlo de forma descendente. Luego ordenar ese mismo arreglo 
de forma aleatoria. Utilizando array en Pythonimport array"""

import array
import random

lista = array.array('i', [9, 2, 10, 14, 3])

#Ordenando arreglo de forma descendente
lista = sorted(lista, reverse=True)
print("Arreglo descendente:",lista)

#Ordenando arreglo de forma aleatoria
random.shuffle(lista)
print("Arreglo aleatorio:",lista)
