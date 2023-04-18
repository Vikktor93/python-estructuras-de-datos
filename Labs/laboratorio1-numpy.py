import numpy as np

#Función que solicita los elementos de la matriz por consola
def elementos_matriz(filas, columnas):
    m = np.zeros((filas, columnas))
    for i in range(filas):
        for j in range(columnas):
            m[i][j] = int(input(f"Elemento ({i+1}, {j+1}): "))
    return m

#Resta de las 2 matrices
def resta_matrices(m1, m2):
    return m1 - m2

#Suma de las 2 matrices
def suma_matrices(m1, m2):
    return m1 + m2

#Se solicita la cantidad de filas y columnas por consola
filas = int(input("Ingrese la cantidad de filas de la matriz: "))
columnas = int(input("Ingrese la cantidad de columnas de la matriz: "))

#Se crea la primera matriz
print("Ingrese los elementos de la primera matriz:")
m1 = elementos_matriz(filas, columnas)

#Se crea la segunda matriz
print("Ingrese los elementos de la segunda matriz:")
m2 = elementos_matriz(filas, columnas)


#Se resta las 2 matrices y se imprime
matriz_final = resta_matrices(m1, m2)
print("La resta de las matrices es:")
print(matriz_final)

#Se suma las 2 matrices y se imprime
matriz_final = suma_matrices(m1, m2)
print("La suma de las matrices es:")
print(matriz_final)

