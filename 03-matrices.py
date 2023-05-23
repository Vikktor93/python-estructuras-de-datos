### GUIA RÁPIDA MATRICES EN PYTHON ###
# Docente: Victor Saldivia Vera - Institución: Universidad de Los Lagos

import numpy as np

#Declarando una matriz con elementos y otra vacia
m1 = [[1,2,3],[4,5,6]]
m2 = []

print('Matriz 1:', m1)

#Consultando elementos de la matriz y filas
print("Segunda fila Matriz:", m1[1])
print("Tercer elemento de la segunda fila:", m1[1][2])
print("Último elemento de la primera fila:", m1[0][-1])

#Consultando una columna
c = 1 #Columna que queremos obtener
columna = []
for fila in m1:
	columna.append(fila[c])
print('Segunda Columna:',columna)

print("############## MULTIPLICACION MATRICES ##############")
#Matriz identidad
mi = np.eye(3,dtype=int)  #Matriz identidad de 3x3

#Matriz aleatoria
m_random = np.random.randint(1, 10, size=(3, 3), dtype=int)  #Matriz aleatoria de 3x3

#Multiplicación de las matrices
m_final= np.dot(mi, m_random)

# Imprimir las matrices
print("\nMatriz Identidad:")
for i in mi:
	print(i)

print("\nMatriz Aleatoria:")
for i in m_random:
	print(i)

print("\nMatriz Final obtenida de la multiplicación:")
for i in m_final:
	print(i)


print("\n\n############## MATRICES TRANSPUESTAS ##############")
# Definir una matriz
m3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

#Matriz Transpuesta
mt = np.transpose(m3)

#Impresion Matriz y Transpuesta
print("\nMatriz original:")
for i in m3:
	print(i)

print("\nMatriz transpuesta:")
for i in mt:
	print(i)
