#examen 3 parcial
#Gabriela Sanchez Alcaraz

import networkx as nx
import matplotlib.pyplot as plt


# clase para representar un nodo/vertice de un grafo
class Vertice:
    def __init__(self, n):
        self.n = n
        self.nombre = n  # nombre de los nodos a los que se conecta un nodo

        # C <- A -> B
        #      ↓         vecinos de A = [B, C, D]
        #      D
        self.vecinos = list()
        self.distancia = 0
        self.color = 'blanco'
        self.pred = -1
        self.next = None
        self.tiempo_descubrimiento = 0 # d tiempo de descubrimiento
        self.tiempo_termino = 0 # f tiempo de termino

    # agregar un nodo/vertice a la lista de vecinos del nodo
    def agregar_vecino(self, v):
        if v not in self.vecinos:  # si v no existe en vecinos del nodo, ai agregarlo
            self.vecinos.append(v)  # agregar a lista
            self.vecinos.sort()  # ordenar lista


# clase para representar un grafo con sus nodos/vertices
class Grafo:
    def __init__(self):
        # diccionario que guarda el valor de vertice
        # {A : memoria, B : memoria, C : memoria, D : memoria }
        # memoria indica donde esta guardado el nodo
        self.vertices = {}
        self.tiempo = 0
        self.node = [None] * 6
        self.next = None

    # agregar un vertice o nodo al grafo
    def agregar_vertice(self, vertice):
        # si el vertice si es una instancia de la clase Vertice y su
        # nombre no se encuentra ya en la lista de vertices, si agregarlo al diccionario
        # (la llave es su nombre y su valor es la instancia/espacio en memoria)
        if isinstance(vertice, Vertice) and vertice.nombre not in self.vertices:
            self.vertices[vertice.nombre] = vertice
            return True
        else:
            return False

    # agregar un arista al un vertice o nodo
    # u y v son nodos/vertices
    # este metodo es para grafos NO DIRIGIDOS porque agrega aristas
    # en ambos sentidos (u, v) y (v, u) o u ↔ v
    def agregar_arista_no_dirigido(self, u, v):
        # si ambos nodos/vertices existen en el diccionario de vertices
        # del grafo, si es una conexión valida

        # al recorrer el diccionario, si la llave es igual al nodo/vertice u,
        # al valor (que es el espacio de memoria de u) llamarle el metodo
        # de agregar_vecino para agregar a v como vecino de u.

        # lo anterior aplica para el nodo/vertice v
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.agregar_vecino(v)
                if key == v:
                    value.agregar_vecino(u)
            return True
        else:
            return False

    # agregar un arista al un vertice o nodo
    # u y v son nodos/vertices
    # este metodo es para grafos DIRIGIDOS porque agrega arista
    # en un sentido (u, v) o u -> v
    def agregar_arista_dirigido(self, u, v):
        # si ambos nodos/vertices existen en el diccionario de vertices
        # del grafo, si es una conexión valida

        # al recorrer el diccionario, si la llave es igual al nodo/vertice u,
        # al valor (que es el espacio de memoria de u) llamarle el metodo
        # de agregar_vecino para agregar a v como vecino de u.

        # lo anterior NO aplica para el nodo/vertice v, ya que
        # la conexion va en una sola direccion
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.agregar_vecino(v)
            return True
        else:
            return False

    # imprimir cada vertice y la lista de sus vecinos
    def imprimir_grafo(self):
        for key in sorted(list(self.vertices.keys())):
            print(f"Vertice {key}\nSus vecinos son {self.vertices[key].vecinos}\n")

    '''dibujar un grafo no dirigido'''
    def visualizar_grafo_no_dirigido(self):
        G = nx.Graph()  # crear instancia de grafo no dirigido
        G.add_nodes_from(self.vertices.keys())  # agregar vertices a grafo
        edges = []  # lista que guarda todas las aristas del grafo

        # colocar la llave y sus respectivo vecino(s) juntos,
        # para formar una tupla con el arista, y esta tupla
        # se agregue a la lista de edges que es la lista de
        # todos los aristas del grafo
        for key, value in self.vertices.items():
            for vecino in value.vecinos:
                edges.append((key, vecino))
        G.add_edges_from(edges)
        # visualizar el grafo
        nx.draw_circular(G, with_labels=True, font_weight="bold")

        plt.show()

        A = nx.adjacency_matrix(G)
        print(f'{A.todense()}\n')


    '''dibujar un grafo dirigido'''
    def visualizar_grafo_dirigido(self):
        DG = nx.DiGraph() # crear instancia de grafo dirigido
        DG.add_nodes_from(self.vertices.keys())  # agregar vertices a grafo
        edges = []  # lista que guarda todas las aristas del grafo

        # colocar la llave y sus respectivo vecino(s) juntos,
        # para formar una tupla con el arista, y esta tupla
        # se agregue a la lista de edges que es la lista de
        # todos los aristas del grafo
        for key, value in self.vertices.items():
            for vecino in value.vecinos:
                edges.append((key, vecino))
        DG.add_edges_from(edges)

        # visualizar el grafo
        nx.draw_circular(DG, with_labels=True, font_weight="bold")
        plt.show()
        A = nx.adjacency_matrix(DG)
        print(f'{A.todense()}\n')

    def bfs(self, grafo, vertice_inicio):
        print(f'BFS DESDE: {vertice_inicio.nombre}')
        # desplegar la distancia a cada uno de los vertices a partir del vertice.
        for k, v in grafo.vertices.items():
            v.color = 'blanco'
            v.distanica = 0
            v.pred = None

        # se inicializa que al principio empiecen en gris, con ninguna distancia recorrida
        vertice_inicio.color = 'gris'
        vertice_inicio.distanica = 0
        vertice_inicio.pred = None

        keys = list(grafo.vertices.keys())
        values = list(grafo.vertices.values())
        Q = [vertice_inicio]

        while len(Q) != 0:
            u = Q.pop(0)
            for vecino in u.vecinos:
                index = keys.index(vecino)
                v = values[index]

                if v.color == 'blanco':
                    v.color = 'gris'
                    v.distanica = u.distanica + 1
                    u.pred = u
                    Q.append(v)
                    print(f'    Vertice: {v.nombre}')
                    print(f'    Distancia: {v.distanica}\n')


    def dfsVisitar(self, vert):
        '''Funcion para saber por que vertices ha pasado'''
        global tiempo
        tiempo = tiempo + 1
        vert.tiempo_descubrimiento  = tiempo
        vert.color = 'gris'
        # por cada vertice, si esta en blanco significa que no ha pasado por ahi, una vez que pasa se pone como negro
        # se suma el tiempo del recorrido por cada vertice que visita
        for v in vert.vecinos:
            if self.vertices[v].color == 'blanco':
                self.vertices[v].pred = vert
                self.dfsVisitar(self.vertices[v])
        vert.color = 'negro'
        tiempo = tiempo+1
        vert.tiempo_termino = tiempo

    def dfs (self):
        '''Si en el recorrido el vertice esta en blanco sig. que no ha pasado por ahi'''
        global tiempo
        tiempo = 0
        for u in sorted(list(self.vertices.keys())):
            if self.vertices[u].color == 'blanco':
                self.dfsVisitar(self.vertices[u])

    def imprimeGrafoDFS(self):
        '''Funcion que imprime el paso que hizo para descubrir el primero vertice, y cuanto recorre del sig. al original
        del Grafo FDS'''
        for key in sorted(list(self.vertices.keys())):
            print(f'\nVertice: {key}')
            print(f'Descubrimiento/Termino: {str(self.vertices[key].tiempo_descubrimiento)} / {str(self.vertices[key].tiempo_termino)}')

def gradoEntradaSalida(lista, n): #se crea una lista con una longitud
    entrada = [0] * n
    salida = [0] * n

    for i in range(0, len(lista)): #se recorre la lista

        List = lista[i]

        #El grado para el i vértice será el num de caminos directos a los otros vertices

        salida[i+1] = len(List)
        for j in range(0, len(List)):
            # Por cada vertice que tenga una entrada en i
            entrada[List[j]] += 1
    #Se imprimen las entradas y salidas
    print("Vertice\tEntrada\tSalida")

    for k in range(1, n):
        print(str(k) +'\t'+ "\t" + str(entrada[k]) + '\t'+"\t" + str(salida[k]))

if __name__ == "__main__":

    g = Grafo()
    a = Vertice('A')
    g.agregar_vertice(a)
    for i in range(ord('A'), ord('F')):
        g.agregar_vertice(Vertice(chr(i)))

    # Nombres=
    # Alejandra = A
    # Beatriz = B
    # Cesar = C
    # Dania = D
    # Ernesto = E

    edges = ['AB', 'AC', 'AD', 'BD', 'CB', 'CE', 'DA', 'DC', 'DE', 'EA', 'EB']

    for edge in edges:
        g.agregar_arista_dirigido(edge[:1], edge[1:])

    for k, v in g.vertices.items():
        print('%s -> %s' % (k, v.vecinos))

    # Alejandra domina a: Beatriz, Cesar, Dania
    # Beatriz domina a: Dania
    # Cesar domina a: Beatriz y Ernesto
    # Dania domina a: Alejandra, Cesar y Ernesto
    # Ernesto domina a: Alejandra y Beatriz

    #A1   B2   C3   D4   E5
    g.imprimir_grafo()
    g.visualizar_grafo_dirigido()

    lista_grado = []

    lista_grado.append([2, 3,4]) # se va agregando el vertice de salida al 1 ' Alejandra'

    lista_grado.append([4]) # se va agregando el vertice de salida al 2 "beatriz'

    lista_grado.append([2,5])

    lista_grado.append([1,3,5])
    lista_grado.append([1,2])


    n = len(lista_grado)+1
    gradoEntradaSalida(lista_grado, n)
    print('El lider del Grupo es Alejandra Y Dania porque su grado de entrada - grado de salida, son mayores que los '
          'demas integrantes  ')
#Examen Gabriela Sanchez Tijuana, Baja California