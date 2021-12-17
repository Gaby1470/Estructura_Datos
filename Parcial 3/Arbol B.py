# Gabriela Sánchez Alcaraz
# Binary B Tree

# Esteban Rodarte 19457
# Gaby Sanchez 33229
# Jorge Matsumoto 27808


class Nodo:
    """Clase nodo a utilizar para el árbol b"""
    def __init__(self, t):  # t es el grado_mínimo, min de hijos
        """Inicialización de los atributos"""
        self.keys = list()
        self.child = list()
        self.hoja = True
        self.n = 0  # números de valores o keys que tiene el nodo
        for _ in range(2*t+1):  # es el maximo de hijos, +1 para tener un espacio extra con NONE
            self.keys.append(None)
        for _ in range(2*t+1):
            self.child.append(None)

    # def __str__(self):
    #     for i in range(2 * self.n):
    #         if self.llaves[i] is not None:
    #             print(self.llaves[i], end=' ')
    #     return str()


class ArbolB:
    """Clase árbol que administra los nodos"""
    def __init__(self, grado_min):
        """Inicialización de los atributos del árbol"""
        self.t = grado_min
        self.root = Nodo(self.t)

    # def create(self):
    #     if self.raiz is None:  # si la clase esta vacía
    #         self.raiz = Nodo(self.t)  # la raíz se inserta el valor del mínimo
    #     return self.raiz

    def splitshild(self, x, i):
        """divide el nodo si a la mitad si ya esta lleno (tiene 4 valores)"""
        z = Nodo(self.t)
        y = x.child[i - 1]  # nunca toca el espacio 5, siempre lo dejara en NONE
        z.hoja = y.hoja
        z.n = self.t  # la cantidad de llaves en el nodo siempre es el grado mínimo

        for j in range(self.t):  # lo recorre por numero de grado mínimo
            z.keys[j] = y.keys[j + self.t + 1]  # la hoja de z en la posición j toma el valor de x.hijos en la posición
            # j+t+1(iteración+grado mínimo+1)
            y.keys[j + self.t + 1] = None

        if y.hoja:
            for j in range(self.t+1):  # se cambian los valores de los hijos de las divisiones
                z.child[j] = y.child[j + self.t]
                y.child[j + self.t] = None
        y.n = self.t
        for j in range(x.n+1, i, -1):  # se cambian los valores de los hijos del nodo creado
            x.child[j] = x.child[j - 1]
        x.child[i] = z  # changed from  x.hijos[i+1] = z

        for j in range(x.n, i-1, -1):  # se cambian los valores de las llaves del nodo creado
            x.keys[j] = x.keys[j - 1]
        x.keys[i - 1] = y.keys[self.t]
        y.keys[self.t] = None
        x.n += 1

    def insert_nonfull(self, x, k):
        """Función que inserta un valor en un nodo que no se encuentra vacío"""
        i = x.n  # i es la posición en donde se va a insertar el valor
        if x.hoja:  # si x es nodo hoja
            while (i >= 1) and (x.keys[i - 1] is not None and k < x.keys[i - 1]):  # mientras la posición sea mayor a 1
                # y las llaves no estén vacías y el valor a insertar sea menor que las llaves.
                x.keys[i] = x.keys[i - 1]
                i -= 1
            if i == 0:  # si la posición es igual a cero
                x.keys[0] = k  # la llave en posición 0 toma el valor de k
                x.n += 1  # se aumenta el valor de posición donde se inserta el valor
            else:
                x.keys[i] = k  # se agrega el valor en la posición de i
                x.n += 1  # se aumenta el valor de posición donde se inserta el valor
        else:  # se determina en que lugar de hijos irá el valor a insertar si no es nodo hoja
            while (i >= 1) and (x.keys[i - 1] is not None and k < x.keys[i - 1]):
                i -= 1
            if x.child[i].n == 2*self.t+1:
                self.splitshild(x, i)
                if x.keys[i] is not None and k > x.keys[i]:
                    i += 1
            self.insert_nonfull(x.child[i], k)
            if x.child[i].n == 2*self.t+1 and x.n < 2*self.t:  # se hace el split si la cantidad de valores es 5
                self.splitshild(x, i+1)

    def insert(self, k):
        """Insertar valores, función que maneja las otras funciones de insertar"""
        r = self.root
        # print(r.llaves, r.hijos)
        if r.n == 2*self.t and r.hoja:  # si la cantidad de valores en la raíz es igual a 2**grado mínimo
            s = Nodo(self.t)
            self.root = s  # la raíz es ahora el nuevo nodo creado
            s.hoja = False  # se establece que la nueva raíz no es un nodo hoja
            s.n = 0
            s.child[0] = r
            self.insert_nonfull(s, k)  # se agrega el valor y se divide en esta función
            # self.splitshild(s, 1)
            # self.insert_nonfull(s, k)
        else:
            self.insert_nonfull(r, k)  # si la raíz esta llena, se manda el insertar cuando esta lleno por recursividad

    def search(self, nodo, k):
        """Función que permite la búsqueda de un valor en el árbol"""
        if nodo:  # solo se busca en nodos existentes
            x = nodo
            i = 0  # es la posición en la que se encuentra el nodo
            while i <= x.n and (x.keys[i] is not None and k > x.keys[i]):
                i += 1
            # print(f"i = {i}, llaves = {x.llaves}")
            if i <= x.n and k == x.keys[i]:
                return x, i  # regresa el nodo y su posición en el nodo
            else:
                if x.hoja:  # si no se encuentra el valor y el nodo es una hoja entonces el valor no está en el árbol
                    return None
                else:
                    return self.search(x.child[i], k)  # si no encuentra el valor en la raíz, se utiliza la recursividad
                    # en los hijos


if __name__ == "__main__":  # se crean las pruebas del código
    bt = ArbolB(2)  # se crea una instancia de árbol b con un grado mínimo de 2
    print("Nodo Creado")
    bt.insert(111)  # se prueba que se puede insertar un valor en un nodo
    bt.insert(96)
    bt.insert(84)
    bt.insert(16)
    bt.insert(999)  # se comprueba la inserción cuando la raíz esta llena y se crea una nueva raíz

    bt.insert(34)
    bt.insert(74)
    bt.insert(356)
    bt.insert(42)  # se comprueba la inserción cuando el nodo hoja está lleno y la raíz contiene un valor

    bt.insert(75)
    bt.insert(76)
    bt.insert(112)
    bt.insert(113)
    bt.insert(77)
    bt.insert(35)
    bt.insert(36)
    # bt.insert(37)

    print("raiz =", bt.root.keys)  # se imprime el valor de la raíz y sus hijos
    for node in bt.root.child:
        if node:
            print(node.llaves)
        else:
            print("None")

    busqueda = bt.search(bt.root, 999)  # se comprueba que la función búsqueda funcione adecuadamente
    print(f"search = {busqueda[0].llaves}, {busqueda[1]}")
# Ultima actuaización 9/11/2021 | Tijuana, Baja California.
# Gabriela Sánchez Alcaraz
