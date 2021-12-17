#Code Insertion Sort
#Gabriela Sanchez Alcaraz 33229, Iram Abbud 033150, Stephanie Gonzalez 33892, Gustavo Lopez 33225

from random import randint

#se crea una funcion que haga el insertion sort
def Insertion_Sort(array):
    for i in range(1,len(array)): #recorre el arreglo segun el largo de la lista.
        aux = array[i] #se guarda en una variable el numero segun el indice a partir del 1
        a = i-1 #el numero a la izq. del indice que se desea comparar
        while a>=0 and array[a] > aux: #si el aux es menor que a  mueve a su izq. y se sigue comparando hasta que el
        #num [a] a su izquierda sea mayor que aux
            array[a+1] = array[a] #se mueven los numeros al indice de la derecha para que aux entre en a
            a -= 1
        array[a+1] = aux
        print(f"{aux}, es el numero comparado y la lista quedó: {array}")

lista = [] #se crea una lista vacia

Switch = True
while(Switch):
    arrLength = int(input("Cantidad de Elementos: ")) # Se le pide al usuario insertar el tamaño del arreglo
    # VALIDACIÓN  DE ENTERO N
    if arrLength<=0 or arrLength>50:
        print("Tamano invalido. Tamano valido: 1 a 50")
    else:
        #GENERACIÓN DE ARREGLO ALEATORIO
        arrayNumbers = [randint(0, 101) for i in range(arrLength)]
        Switch = False
        # DESPLIEGUE DE DATOS
        print("El arreglo de", arrLength, "elementos es: ", arrayNumbers)
        Insertion_Sort(arrayNumbers)
        print("\nEl Arreglo Ordenado: ", arrayNumbers)

#Ultima modificación 24/08/2021 Gabriela Sánchez Alcaraz
#Iram Abbud, Stephanie Gonzalez, Gustavo Lopez