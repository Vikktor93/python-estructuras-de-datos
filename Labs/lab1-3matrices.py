import random

"""Laboratorio 1: Crear un algoritmo donde se solicite dos matrices por consola. Tanto la cantidad de columnas 
como de filas, deben ser ingresadas por teclado. Los elementos de las matrices deben ser generados de forma 
aleatoria (0 al 5). Estas dos matrices se deben sumar. Luego se solicita una tercera matriz. Al igual que las 
dos anteriores, se ingresan columnas y filas por consola, y sus elementos son generados aleatoriamente (0 a 5). 
Esta última matriz se restará con la matriz resultante entre la operación de suma."""

#Se solicita la cantidad de filas y columnas de las primeras dos matrices
filas = int(input("Ingrese la cantidad de filas de las matrices: "))
columnas = int(input("Ingrese la cantidad de columnas de las matrices: "))

#Se generan las dos primeras matrices aleatorias
m1 = [[random.randint(0, 5) for j in range(columnas)] for i in range(filas)]
#print(m1)

m2 = [[random.randint(0, 5) for j in range(columnas)] for i in range(filas)]

#Suma de las dos matrices
suma = [[m1[i][j] + m2[i][j] for j in range(columnas)] for i in range(filas)]

#Se solicita la cantidad de filas y columnas de la 3°ra matriz
filas3 = int(input("Ingrese la cantidad de filas de la tercera matriz: "))
columnas3 = int(input("Ingrese la cantidad de columnas de la tercera matriz: "))

#3ra matriz aleatoria
m3 = [[random.randint(0, 5) for j in range(columnas3)] for i in range(filas3)]

#Resta de la 3°ra matriz a la suma de las dos matrices anteriores
resta = [[suma[i][j] - m3[i][j] for j in range(columnas)] for i in range(filas)]

#Resultados
print("Matriz 1:")
for i in range(filas):
    for j in range(columnas):
        print(m1[i][j], end=" ")
    print()

print("\nMatriz 2:")
for i in range(filas):
    for j in range(columnas):
        print(m2[i][j], end=" ")
    print()

print("\nSuma de las dos primeras matrices:")
for i in range(filas):
    for j in range(columnas):
        print(suma[i][j], end=" ")
    print()

print("\nMatriz 3:")
for i in range(filas3):
    for j in range(columnas3):
        print(m3[i][j], end=" ")
    print()

print("\nResta entre la matriz resultante y la tercera matriz:")
for i in range(filas):
    for j in range(columnas):
        print(resta[i][j], end=" ")
    print()
