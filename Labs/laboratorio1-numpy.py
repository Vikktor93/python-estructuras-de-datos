import numpy as np

def suma(m1, m2):
    m_final_suma = np.add(m1, m2)
    return m_final_suma

def resta(m1, m2):
    m_final_resta = np.subtract(m1, m2)
    return m_final_resta

filas = int(input("Ingrese la cantidad de filas de la matriz: "))
columnas = int(input("Ingrese la cantidad de columnas de la matriz: "))

#Ingreso de elementos Matriz 1
print("Ingresando los elementos de la matriz 1:")
m1 = np.zeros((filas, columnas)) 
for i in range(filas):
    for j in range(columnas):
        elem  = int(input(f"Ingrese el elemento [{i}][{j}]: "))
        m1[i][j] = elem

#Ingreso de elementos Matriz 2
print("\nIngresando los elementos de la matriz 2:")
m2 = np.zeros((filas, columnas)) 
for i in range(filas):
    for j in range(columnas):
        elem = int(input(f"Ingrese el elemento [{i}][{j}]: "))
        m2[i][j] = elem

#Suma Matrices
m_final_suma = suma(m1, m2)
print("\nLa matriz resultado de la suma es:")
print(m_final_suma)

#Resta Matrices
m_final_resta = resta(m1, m2)
print("\nLa matriz resultado de la resta es:")
print(m_final_resta)
