#Shell Binary Sort
#Juan de la Torre 33162, Stephanie Gonzalez 33892 y Gabriela Sánchez Alcaraz 33229

#Funcion que con una lista la divide entre dos y va comparando el primer elemento de cada subarreglo, si el subarreglo 1
#en el indice 0 es mayor al subarreglo 2 en indice 0, se cambian de posicion, si es menor se queda igual.
def ShellSort(array):
    inte = len(array)#variable donde se guarda el largo del arreglo
    while inte > 1:
        inte = (inte//2) #divide el arreglo en 2
        band = True
        while band == True:
            band = False
            i = 0
            while i+inte <= len(array)-1:
                if array[i] > array[i + inte]: #revisa si el subarreglo 1[0] es mayor al subarreglo 2[0]
                    array[i], array[i + inte] = array[i + inte], array[i]#si es mayor cambian de posicion
                    band = True
                i = i + 1
    return array

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

numeros = []
while True:
    n = int(input("¿De que tamaño quieres tu lista?: "))  # se pide que tan grande la lista será
    if n > 1:  # si la lista es mayor a 1
        numeros = list(map(int, input("Ingresa los numeros de todo tu lista (separados por espacio) : ").split()))  # se piden los numeros dentro del arreglo
        if len(numeros) != n: # Si los numeros ingresados son mas que el numero de tamaño del arreglo
            print("Los numeros ingresados no es el mismo tamaño de la lista. ")
            break
        incognita = int(input("¿Cual numero de la lista deseas buscar?: "))
        print("Esta es tu lista en desorden: ", numeros,)
        print(f"Esta es tu lista ordenada: {ShellSort(numeros)}")#se manda llamar la funcion ShellSort
        busqueda = Binario(numeros,0,len(numeros)-1,incognita) # declaramos la funcion Binario que encuentra el numero en una variable y pone su posicion iniciando en 0
        if busqueda != -1: # Si el numero esta en la lista, se imprime su posicion en la lista
            print("El numero que deseas encontrar esta en la posicion: ", str(busqueda))
        else: # Si no, es que no esta en la lista
            print("El numero que deseas encontrar no esta en la lista.")
        break
    else:  # si el numero es menor a 1
        print("La lista debe ser mayor a 1\n")


#Ultima actualizacion Gabriela Sánchez Alcaraz Tijuana, Baja California
#Estephanie Gonzalez y Juan de la Torre