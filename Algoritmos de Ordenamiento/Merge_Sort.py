#Merge Sort
#Axel Cruz, Jorge Matsumoto, Gabriela Sánchez
import random

#funcion que recive un arrego, lo divide en dos y cada subarreglo lo divide en 2, y se manda llamar la funcion Merge
def MergeSort(a):
    if len(a) == 1:
        return a
    m = len(a)//2
    b = MergeSort(a[:m])
    c = MergeSort(a[m:])
    sorted_array = merge(b ,c)
    return sorted_array

#funcion que si el indice en b es mayor a c, se cambian sus posiciones y el contador aumenta 1 pues se hizo un cambio.
#Ademas agrega los numeros menos a la izq.y los mayores a la derecha

def merge(B, C):
    d = []
    global counter
    while len(B) != 0 and len(C) != 0:
        if B[0] <= C[0]:
            d.append(B.pop(0))#agrega el numero a d y lo elimina con pop de ese indice
        else:
            d.append(C.pop(0))
            counter +=1
    d.extend(B[0:])#extend es como append pero funciona con mas numeros
    d.extend(C[0:])
    return d

lista = []
counter = 0
# def array_input():
while True:
    n = int(input("Que tan grande quires tu arreglo "))  # se pide que tan grande la lista sera
    if 1 <= n <= 106:  # si la lista es mayor a 0 y menor a 106
        for i in range(0, n):  # se crean numeros random segun el largo que la lista sea
            x = random.randint(1, 109)  # los numeros random van del 1-108
            lista.append(x)  # se agregan los numeros random a la lista
        print(f"Original: {lista}")
        print(f"Ordenada: {MergeSort(lista)}")
        print(f"Contador: {counter}")
        #MergeSort(lista)  # se manda llamar la funcion
        break
    else:  # si el numero es menor a 0 o mayor a 50 se manda pedir otra vez un numero hasta hacer la lista.
        print("El numero debe estar entre 1 y 105\n")



#Ultima actualización: Gabriela Sánchez Alcaraz. Tijuana, Baja California. 31/08/2021
#Axel Cruz y Jorge Matsumoto
