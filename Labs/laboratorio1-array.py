from array import *

# Función para pedir los elementos de una matriz por teclado
def pedir_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            elemento = float(input(f"Elemento ({i+1}, {j+1}): "))
            fila.append(elemento)
        matriz.append(fila)
    return matriz

# Función para sumar dos matrices
def sumar_matrices(matriz1, matriz2):
    matriz_resultante = []
    for i in range(len(matriz1)):
        fila = []
        for j in range(len(matriz1[0])):
            suma = matriz1[i][j] + matriz2[i][j]
            fila.append(suma)
        matriz_resultante.append(fila)
    return matriz_resultante

# Función para restar dos matrices
def restar_matrices(matriz1, matriz2):
    matriz_resultante = []
    for i in range(len(matriz1)):
        fila = []
        for j in range(len(matriz1[0])):
            resta = matriz1[i][j] - matriz2[i][j]
            fila.append(resta)
        matriz_resultante.append(fila)
    return matriz_resultante

# Pedimos la cantidad de filas y columnas para ambas matrices
filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))

# Creamos la primera matriz ingresando sus valores por teclado
print("Ingrese los elementos de la primera matriz:")
matriz1 = pedir_matriz(filas, columnas)

# Creamos la segunda matriz ingresando sus valores por teclado
print("Ingrese los elementos de la segunda matriz:")
matriz2 = pedir_matriz(filas, columnas)

# Sumamos las dos matrices y mostramos el resultado
matriz_resultante = sumar_matrices(matriz1, matriz2)
print("La suma de las matrices es:")
for fila in matriz_resultante:
    print(fila)

# Restamos las dos matrices y mostramos el resultado
matriz_resultante = restar_matrices(matriz1, matriz2)
print("La resta de las matrices es:")
for fila in matriz_resultante:
    print(fila)