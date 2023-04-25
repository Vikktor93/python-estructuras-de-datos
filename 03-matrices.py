### GUIA RÁPIDA MATRICES EN PYTHON ###
# Docente: Victor Saldivia Vera - Institución: Universidad de Los Lagos

#Declarando una matriz con elementos y otra vacia
m1 = [[1,2,3],[4,5,6]]
m2 = []

print('Matriz 1:', m1)

#Consultando elementos de la matriz y filas
print("Segunda fila Matriz:", m1[1])
print("Tercer elemento de la segunda fila:", m1[1][2])
print("Último elemento de la primera fila:", m1[0][-1])

#Consultando una columna
z = 1 #Columna que queremos obtener
columna = []
for fila in m1:
	columna.append(fila[z])
print('Segunda Columna:',columna)

