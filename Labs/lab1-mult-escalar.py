import random

"""Laboratiorio 1: Crear una matriz la cual se debe solicitar por teclado la cantidad de filas 
y columnas que va a contener. También ingresar por consola un escalar. Los elementos de la matriz 
deben ser generados aleatoriamente (0 al 10). Por último, se debe multiplicar la matriz generada 
por el escalar ingresado."""

filas = int(input("Ingrese la cantidad de filas de la matriz: "))
columnas = int(input("Ingrese la cantidad de columnas de la matriz: "))
escalar = int(input("Ingrese el escalar: "))

#Matriz Random
m = [[random.randint(0, 10) 
           for j in range(columnas)] 
           for i in range(filas)]


#Impresión matriz original
print("\nMatriz original:")
for fila in m:
    print(fila)
print("\n")

#Multiplicación de cada elemento de la matriz por el escalar
resultado = [[elem * escalar for elem in fila] for fila in m]

# Imprimimos el resultado
print("Matriz final:")
for fila in resultado:
    print(fila)
