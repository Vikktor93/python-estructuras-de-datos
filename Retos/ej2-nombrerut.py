"""Crear un algoritmo que permita guardar los nombres y el RUT 
de 5 personas sin perder ninguna de ellas. El usuario tiene que 
ingresar la información de cada persona por consola.
Se debe imprimir los arrays de nombres y RUT para luego ordenarlas 
alfabéticamente y ascendentemente respectivamente.
"""
#Inicialización de las listas
nombres = []
rut = []

#Definición de tamaño 5 de la list<
tam = 5

#Leemos los datos y los agregamos a la lista
for i in range(tam):
    print("Ingrese los datos de la persona", i + 1)
    nombre = input("Nombre: ")
    cedula = input("RUT: ")

    nombres.append(nombre)
    rut.append(cedula)

#Imprimiendo los elementos de la lista
print("\n")
print("##### MOSTRANDO LOS DATOS DE LAS PERSONAS #####")

#se ordena la lista con sort()
nombres.sort()

#ciclo
for i in range(tam):
    print("Datos de la persona N°",i + 1)

    print("Nombre:", nombres[i])
    print("RUT:", rut[i])
    print("\n")

print("\n")
print("##### MOSTRANDO LOS DATOS DE LAS PERSONAS ORDENADOS#####")
for i in range(tam):
    print("Datos de la persona N°",i + 1)

    print("Nombre:", nombres[i])
    print("RUT:", rut[i])
    print("\n")