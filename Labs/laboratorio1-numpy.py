import numpy as np

#Función para pedir los elementos de una matriz por teclado
def pedir_matriz(filas, columnas):
    matriz = np.zeros((filas, columnas))
    for i in range(filas):
        for j in range(columnas):
            matriz[i][j] = float(input(f"Elemento ({i+1}, {j+1}): "))
    return matriz

# Función para sumar dos matrices
def sumar_matrices(matriz1, matriz2):
    return matriz1 + matriz2

# Función para restar dos matrices
def restar_matrices(matriz1, matriz2):
    return matriz1 - matriz2

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
print(matriz_resultante)

# Restamos las dos matrices y mostramos el resultado
matriz_resultante = restar_matrices(matriz1, matriz2)
print("La resta de las matrices es:")
print(matriz_resultante)
