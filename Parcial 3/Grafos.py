# Grafos
# Gabriela Sanchez Alcaraz

class Vertice:
    def __init__(self, n):
        self.nombre = n
        self.vecinos = list()
        self.distancia = 0
        self.color = 'blanco'
        self.pred = -1

        self.tiempo_descubrimiento = 0
        self.tiempo_termino = 0

    def agregarVecino(self, v):
        if v not in self.vecinos:
            self.vecinos.append(v)
            self.vecinos.sort()


class Grafo:
    def __init__(self):
        self.vertices = {}
        self.tiempo = 0

    def agregarVertices(self, vertice):
        if isinstance(vertice,Vertice) and vertice.nombre not in self.vertices: # checa si es una instancia, y regresa
            # si es True o False, y si no esta el nombre en el vertice
            self.vertices[vertice.nombre] = vertice # se agrega el nombre al vertice
            return True
        else:
            return False

    def agregarAristaNoDirigido(self, u, v): # (i,j) -> origen,destino
        '''Grafo no dirigido'''
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items(): # por cada key y value en el diccionario
                if key == u: # si key es lo mismo a u
                    value.agregarVecino(v) # se agrega
                if key == v:
                    value.agregarVecino(u)
            return True
        else:
            return False

    def agregarAristaDirigido(self, u, v): # (i,j) -> origen,destino
        '''Grafo Dirigido'''
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items(): # por cada key y value en el diccionario
                if key == u: # si key es lo mismo a u
                    value.agregarVecino(v) # se agrega
            return True
        else:
            return False

    def imprimeGrafo(self):
        for key in sorted(list(self.vertices.keys())):
            print(f"Vertice {key} sus vecinos son: {str(self.vertices[key].vecinos)}")

    def bfs(self, grafo, vertice_inicio):
        print(f'BFS DESDE: {vertice_inicio.nombre}')
        #desplegar la distancai a cada uno de os vertices a partir del vertice
        for k, v in grafo.vertices.items():
            v.color = 'blanco'
            v.distanica = 0
            v.pred = None

        vertice_inicio.color = 'gris'
        vertice_inicio.distanica = 0
        vertice_inicio.pred = None

        keys = list(grafo.vertices.keys())
        values = list(grafo.vertices.values())
        Q = [vertice_inicio]

        while len(Q) != 0:
            u = Q.pop(0)
            for vecino in u.vecino:
                index = keys.index(vecino)
                v = values[index]

                if v.color == 'blanco':
                    v.color = 'gris'
                    v.distanica = u.distanica +1
                    u.pred = u
                    Q.append(v)
                    print(f'    Vertice: {v.nombre}')
                    print(f'    Distancia: {v.distanica}\n')

# g = Grafo()
# a = Vertice('A')
# g.agregarVertices(a)
# for i in range(ord('A'),ord('K')):
#     g.agregarVertices(Vertice(chr(i)))
#
# edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'GJ']
#
# for edge in edges:
#     g.agregarArista(edge[:1], edge[1:])
#
# for k,v in g.vertices.items():
#     print('%s -> %s'%(k,v.vecinos))

'''Ejercicio Lista Adyacencia (Grafo NO Dirigido)'''
# g = Grafo()
# a = Vertice('1')
# g.agregarVertices(a)
# for i in range(ord('1'),ord('6')):
#     g.agregarVertices(Vertice(chr(i)))
#
# edges = ['12', '21','15','51', '25','52','24','42','23','32','34','43','54','45']
#
# for edge in edges:
#     g.agregarAristaNoDirigido(edge[:1], edge[1:])
#
# for k,v in g.vertices.items():
#     print('%s -> %s'%(k,v.vecinos))

'''Ejercicio Lista Adyacencia (Grafo Dirigido)'''
g = Grafo()
a = Vertice('1')
g.agregarVertices(a)
for i in range(ord('1'),ord('7')):
    g.agregarVertices(Vertice(chr(i)))

edges = ['12','14','25','42','54','35','36']

for edge in edges:
    g.agregarAristaDirigido(edge[:1], edge[1:])

for k,v in g.vertices.items():
    print('%s -> %s'%(k,v.vecinos))


# Ultima Actualizacion 11/18/2021 | Tijuana, Baja California
