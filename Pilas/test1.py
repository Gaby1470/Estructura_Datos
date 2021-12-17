#Programa que recibe un string del usuario y lo invierte mediante una Pila

class pila():
    def __init__(self, size):
        self.list = []
        self.size = size
        self.top = -1

    def IsEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def IsFull(self):
        if self.size == self.top+1:
            return True
        else:
            return False

    def Insert(self, value):
        if not self.IsFull():
            self.list.append(value)
            self.top+=1

    def Delete(self):
        if not self.IsEmpty():
            self.list.pop(self.top)
            self.top-=1

def InvierteString(string, length):
    p = pila(length)
    for char in string:
        p.Insert(char)

    while not p.IsEmpty():
        print(p.list[p.top], end="")
        p.Delete()

palabra = (input("Escriba una palabra u oracion: "))
length = len(palabra)
InvierteString(palabra, length)