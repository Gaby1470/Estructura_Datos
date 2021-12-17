#Implementancion de Pilas estaticas en listas

class Pilas():
    def __init__(self, size):
        self.lista = []
        self.size = size
        self.top = -1

    def IsEmpty(self): #revisa que la lista no esta vacia
        if self.top == -1:
            return True
        else:
            return False

    def IsFull(self): #revisa que la lista no este llena
        if self.size == self.top + 1:
            return True
        else:
            return False

    def InserElement(self, item): #se agrega un Item a la lista
        if not self.IsFull():
            self.lista.append(item)
            self.top =+ 1 #El ultimo elemento se agrega 1, porque la lista ya tiene 1 dato mas

    def DeleteElement(self, item):
        if not self.IsEmpty():
            self.lista.pop(self.top) #siempre borramos el ultimo de la lista (self.top)
            self.top =-1

if __name__ == '__main__':
    p = Pilas(size=7)
    print(p.IsEmpty())
    p.InserElement(4)
    print(p) #Imprime la ubicacion de la memoria
    print(f"El primer elemento agregado a la lista: {p.lista}") #Imprime la lista
    p.InserElement(5)
    p.InserElement(10)
    print(p.lista)

