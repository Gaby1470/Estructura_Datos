#Heap Sort
#Gabriela Sánchez Alcaraz

#Se crea la funcion principal donde se pondra el arrelgo principal sin orden.
def heapsort(a):

  heapify(a, len(a)) #se manda llamar la funcion "heapify" donde toma como argumento el arrelgo y su largo

  end = len(a)-1 #end = el largo del arrelgo - 1

  while end > 0: #mientras el largo del arrelgo -1 > 0 entonces:

    a[end], a[0] = a[0], a[end] #el arreglo en el indice "end" se le asigna el valor que hay en el arreglo indice 0
    #y al arreglo en indice 0 se pone el valor que hay en el arreglo indice "end"

    end -= 1 #ahora end vale un valor menos a lo que era antes

    sift_down(a, 0, end) #se llama la funcion "sift_down" y toma como argumentos (el arreglo, 0 y end)

def heapify(a, count): #se hace la funcion que toma como argumentos (el arreglo, y count) que count en este caso es el largo del arreglo

  start = int((count-2)/2) #start = (el largo del arreglo - 2) / 2, y se crean los subarreglos donde se compararan si los valores son menores o mayores

  while start >= 0: #mientras start sea mayor o igual a 0: entonces

    sift_down(a, start, count-1) #se manda llamar la funcion "swift_down", (arreglo, start, y el largo del arreglo-1)

    start -= 1 #se resta el valor de start 1

def sift_down(a, start, end): #se crea la funcion sift_down con argumentos

  root = start #se crea una variable que guarda el valor de start (el largo del arreglo - 2) / 2

  while (root*2+1) <= end: #mientras (el valor de root*2+1) sea menor o igual largo del arrelgo - 1 (end), entoces:

    child = root * 2 + 1 #se crea la variable child = root * 2 + 1

    swap = root #se crea la variable swap = que guarda el valor de root

    if a[swap] < a[child]: #si el arrelgo en indice[swap] es menor al arreglo[child]

      swap = child #entonces swap toma el valor de child

    if (child + 1) <= end and a[swap] < a[child+1]: #si (child + 1) es menor o igual al valor de end y solo y; el valor en
      #en el indice a[swap] es menor a el valor en el indice de a[child+1], entonces:

      swap = child+1 #swap toma el valor de child +1

    if swap != root: #si swap tiene valor DIFERENTE a root, entonces:

      a[root], a[swap] = a[swap], a[root]#se intercambian los valores de a[root] = a[swap] & a[swap] = a[root]

      root = swap #root toma el valor de swap

    else: #si no fue ninguna de las opciones anteriores

      return

    print(a)#se imprime el arreglo


a =[13,6,45,10,3,22,5] #un arreglo de ejemplo
print("Tu lista desordenada:")
heapsort(a) #se manda llamar la funcion con el arrelgo a

print("\nEl ejemplo ya arreglado:\n", a, '\n')

#Ultima Actualizacion Gabriela Sánchez Alcaraz.
#Tijuana, Baja California. 6/septiembre/2021