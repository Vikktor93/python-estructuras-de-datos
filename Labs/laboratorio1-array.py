from array import *

#Función para solicitar los elementos de una matriz por consola
def solicitud_matriz(filas, columnas):
    m = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            elemento = int(input(f"Elemento ({i+1}, {j+1}): "))
            fila.append(elemento)
        m.append(fila)
    return m

#Funcion para restar matrices
def resta_matriz(m1, m2):
    matriz_final = []
    for i in range(len(m1)):
        fila = []
        for j in range(len(m1[0])):
            resta = m1[i][j] - m2[i][j]
            fila.append(resta)
        matriz_final.append(fila)
    return matriz_final

#Funcion para sumar matrices
def suma_matriz(m1, m2):
    matriz_final = []
    for i in range(len(m1)):
        fila = []
        for j in range(len(m1[0])):
            suma = m1[i][j] + m2[i][j]
            fila.append(suma)
        matriz_final.append(fila)
    return matriz_final

#Solicitando la cantidad de filas y columnas de las 2 matrices
filas = int(input("Ingrese la cantidad de filas de la matriz: "))
columnas = int(input("Ingrese la cantidad de columnas matriz: "))

#Creando la 1ra matriz e ingresando los elementos por consola
print("Ingrese los elementos de la primera matriz:")
m1 = solicitud_matriz(filas, columnas)

#Creando la 2da matriz e ingresando los elementos por consola
print("Ingrese los elementos de la segunda matriz:")
m2 = solicitud_matriz(filas, columnas)

#Se restan las dos matrices y se muestra el resultado de la operación
matriz_final = resta_matriz(m1, m2)
print("La resta de las matrices es:")
for fila in matriz_final:
    print(fila)

#Se suman las dos matrices y se muestra el resultado de la operación
matriz_final = suma_matriz(m1, m2)
print("La suma de las matrices es:")
for fila in matriz_final:
    print(fila)

