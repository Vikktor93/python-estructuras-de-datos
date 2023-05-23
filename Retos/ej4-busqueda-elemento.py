"""Reto 4: Crear un arreglo aleatorio de tamaño entre 10 a 30.
Imprimir el arreglo creado y luego solicitar por consola la busqueda de
un elemento en especifico del arreglo creado. Todo esto utilizando import array"""

import array
import random

v = array.array('i',[])

arreglo_random = random.randint(10,30)
print('Creando arreglo random de',arreglo_random,'elementos')
for i in range(arreglo_random):
    v.append(random.randint(10,30))
    
#print('Largo',len(v))
#v.pop()
#print('Nuevo Largo',len(v))

#mostrando el arreglo
for i in range(len(v)):
    print(v[i], end=' ')
    
#Buscando el elemento
print("\n")
elemento = int(input('Elemento a buscar: '))
aux=0
for i in range(len(v)):
    if(v[i]==elemento):
        aux+=1
print('Elemento Encontrado',aux,'veces')




