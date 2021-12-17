#Code Selection Sort
#Daniel Agraz 33293, Gustavo Lopez 33225, Gabriela Sánchez Alcaraz 33229

from random import randint

#Se crea una funcion que en el indice 1 va el num. mas pequeño , y se compararán los num. de dos en dos hasta encontrar
#el menor e intercambiar su posicion con la i

def Selection_Sort(array, n):
    for i in range(n):
        min_index = i
        for j in range(i+1, len(array)):  #n-i se mueve el indice segun en que lugar vayamos de acomodar, i+1, n-1
            if array[min_index] > array[j]:
                min_index = j
        # intercambio de indices entre el menor y el mayor
        array[i], array[min_index] = array[min_index], array[i]
    return array
    

start = 0
stop = 101

n = int(input("Ingresa el tamano de tu arreglo\t"))
numlist = [randint(start, stop) for i in range(n)]
print("Tu arreglo original es:\n", numlist,"\n")
print("Tu arreglo ordenado es:\n", Selection_Sort(numlist, n),"\n")
