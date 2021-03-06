#Ordenamiento Burbuja
#Gabriela Sánchez Alcaraz, Katherine Ramirez Padilla, Alberto Ortega Morales

import random

#se crea una función que cuenta cuantos índices tiene nuestro arreglo

def bubble(numeros):
    n = len(numeros)
    need_change = True #variable que verifica si el array necesita un cambio
    #recorre los elementos de derecha a izquierda
    for i in range(n-1):
        #compara los numeros, si es mayor se cambia la posición, hasta que todos esten en orden
        if need_change: #si no hay necesidad de realizar un cambio en el array la funcion termina
            need_change = False
        for j in range(n-i-1):
            if numeros[j] > numeros[j + 1]:
                need_change = True
                numeros[j], numeros[j +1] = numeros[j+1], numeros[j]#numeros[j] es asignado por numeros[j+1]
#el arreglo
numeros = []
x = int(input('Qué tan grande deseas tu arreglo? ')) #se pregunta que tantos espacios tendrá el arreglo
for i in range(0,x):
    n = random.randint(1,50) #se crea un número aleatoria para cada espacio del arreglo
    numeros.append(n) #se agrega el número al arreglo
print("tu arreglo desordenado:\n",numeros)


#se manda a llamar la función y se imprimen los resultados

bubble(numeros)

print('\n El arreglo con Ordenamiento Burbuja es:')
print(numeros)

#última modificación: Tijuana, Baja California. 17/08/2021. Gabriela Sánchez Alcaraz
#Katherine Ramirez Padilla, Alberto Ortega Morales