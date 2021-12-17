#Quick Sort Binary 1 Parcial
#Gabriela Sánchez Alcaraz

#Se crea la funcion Quick Sort que ordernara el arreglo tomando un pivote a la mitad y los menores los pondra a su izq
#y los mayores a su derecha
def QuickSort(A, l, r):
    if l >= r: #
        return
    m = Partition(A, l, r) #A[m] es la posicion final
    QuickSort(A, l, m)
    QuickSort(A, m + 1, r)
    return A

#esta funcion checa si el num es menor o igual al pivote y cambia su lugar con el indice

def Partition(A, l, r):
    x = A[l] #pivote
    j = l #indice del num mas pequeño
    for i in range (l+1, r):
        if A[i] <= x:
            j = j + 1 #indice cambia +1
            A[j], A[i] = A[i], A[j] #el arreglo A[j] ahora sera A[i]
    A[l], A[j] = A[j], A[l]


    return j



#funcion que encuentra un numero de manera binaria en un arreglo ya en orden
def Binario(array,min, max, incognita):#toma el (arreglo, el numero menor(0), el numero mayor (len(arreglo)+1) y la incognita
    if max >= min:
        mid = (max + min) // 2 #se saca el promedio/la mitad del arreglo
        if array[mid] == incognita: #si la mitad era la incognita se regresa donde se encontro
            return mid
        elif array[mid] > incognita: #si el numero es mayor que el numero a la mitad, se empieza a buscar con la izquierda del arreglo
            #y se vuelve a mandar la funcion Binario y se divide en dos
            return Binario(array,min,mid-1,incognita)
        else:
            return Binario(array, mid+1, max, incognita) #si el numero es mayor que el numero a la mitad, se empieza a
            # buscar con la derecha del arreglo y se vuelve a mandar la funcion Binario y se divide en dos
    else:
        return - 1

#variables
num_list = []
incognitas = []
indices = []
while True:
    #se pide el largo del arreglo y luego sus numeros que iran dentro del arrelgo, con .split cada espacio es un nuevo indice
    n, *num_list =map(int,input("Ingresa el largo de tu arreglo, seguido de los numeros que estaran dentro del arreglo (separado por espacios) ").split())
    #por cada numero en la lista
    for numero in num_list:
        check = numero #en cada vuelta se guarda el numero de esta vuelta en la variable check
        #se checan las restricciones del largo del arreglo, sus numeros en el y que los numeros insertados en el arrelgo no sobrepase su capacidad
        if (1 <= n <= (3 * 10 ** 4)) and num_list not in range(1<= check <= 10**5) and len(num_list)== n :  # si la lista es mayor a 1
            incognitas = map(int,input("Ingresa los numeros que deseas buscar (separados por espacio) : ").split()) #se piden todas las incognitas
            print(f'Tu lista ordenada: {QuickSort(num_list, 0 ,r=len(num_list))}') #se manda llamar quicksort y se impime el arreglo ordenado
            for i in (incognitas): #por cada incognita
                busqueda = Binario(num_list, 0, len(num_list) - 1, i)  # declaramos la funcion Binario que encuentra el numero en una variable y pone su posicion iniciando en 0

                if busqueda != -1:  # Si el numero esta en la lista, se imprime su posicion en la lista
                    print(str(busqueda)," " , end='') #imprime el indice de las incognitas

                else:  # Si no, es que no esta en la lista
                    print("-1")

            break
        else:
            print("El valor de tu arreglo o los elementos que ingresaste no cumplen con las restricciones\n-------------------")
            break

#ultima Actualizacion Gabriela Sánchez Alcaraz
#tijuana, Baja California 14/09/2021