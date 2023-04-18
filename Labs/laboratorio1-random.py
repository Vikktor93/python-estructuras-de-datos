import random

# Función para crear una matriz aleatoria
def matriz_random(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            elemento = random.randint(1, 5) # generamos un número aleatorio entre 1 y 10
            fila.append(elemento)
        matriz.append(fila)
    return matriz

# Función para sumar dos matrices
def suma_matrices(m1, m2):
    matriz_final = []
    for i in range(len(m1)):
        fila = []
        for j in range(len(m1[0])):
            suma = m1[i][j] + m2[i][j]
            fila.append(suma)
        matriz_final.append(fila)
    return matriz_final

# Función para restar dos matrices
def resta_matrices(m1, m2):
    matriz_final = []
    for i in range(len(m1)):
        fila = []
        for j in range(len(m1[0])):
            resta = m1[i][j] - m2[i][j]
            fila.append(resta)
        matriz_final.append(fila)
    return matriz_final

# Creamos dos matrices aleatorias con el mismo tamaño
filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))
print("Creando la primera matriz aleatoria:")
m1 = matriz_random(filas, columnas)
print(m1,"\n")
print("Creando la segunda matriz aleatoria:")
m2 = matriz_random(filas, columnas)
print(m2,"\n")

# Sumamos las dos matrices y mostramos el resultado
matriz_final = suma_matrices(m1, m2)
print("La suma de las matrices es:")
for fila in matriz_final:
    print(fila,"\n")

# Restamos las dos matrices y mostramos el resultado
matriz_final = resta_matrices(m1, m2)
print("La resta de las matrices es:")
for fila in matriz_final:
    print(fila)
