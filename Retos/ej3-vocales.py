"""Ejercicio 3: Escribir un programa que pida al usuario una palabra y muestre por 
pantalla el número de veces que contiene cada vocal."""

palabra = input("Introduce una palabra: ")
vocales = ['a', 'e', 'i', 'o', 'u']
for vocal in vocales: 
    i = 0
    for letra in palabra: 
        if letra == vocal:
            i += 1
    print("La vocal " + vocal + " aparece " + str(i) + " veces")