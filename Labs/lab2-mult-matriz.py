"""Laboratorio 2: Crear un algoritmo que solicite ingresar 2 matrices por teclado. Las columnas y las filas
se deben ingresar por consola al igual que los elementos de cada matriz. Luego se deben multiplicar ambas
matrices."""

#Solicitando las dimensiones de la primera matriz
fila1 = int(input("Ingrese el número de filas de la primera matriz: "))
columna1 = int(input("Ingrese el número de columnas de la primera matriz: "))

#Segunda matriz
fila2 = int(input("Ingrese el número de filas de la segunda matriz: "))
columna2 = int(input("Ingrese el número de columnas de la segunda matriz: "))

#Corroborando si es posible realizar la multiplicación de matrices
if columna1 != fila2:
    print("No se puede realizar la multiplicación de matrices")
else:
    #Creación de las matrices vacias
    m1 = []
    m2 = []
    resultado = []

    #Elementos de la primera matriz
    print("Ingrese los elementos de la primera matriz:")
    for i in range(fila1):
        fila = []
        for j in range(columna1):
            elemento = int(input("Ingrese el elemento [{}, {}]: ".format(i, j)))
            fila.append(elemento)
        m1.append(fila)

    #Elementos de la segunda matriz
    print("Ingrese los elementos de la segunda matriz:")
    for i in range(fila2):
        fila = []
        for j in range(columna2):
            elemento = int(input("Ingrese el elemento [{}, {}]: ".format(i, j)))
            fila.append(elemento)
        m2.append(fila)

    #Inicializando matriz de ceros
    for i in range(fila1):
        fila = []
        for j in range(columna2):
            fila.append(0)
        resultado.append(fila)

    #Multiplicación de matrices
    for i in range(fila1):
        for j in range(columna2):
            for k in range(columna1):
                resultado[i][j] = resultado[i][j] + m1[i][k] * m2[k][j]

    print("El resultado de la multiplicación de matrices es:")
    for fila in resultado:
        print(fila)
