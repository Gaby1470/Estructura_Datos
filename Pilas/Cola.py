class Cola:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def add(self, item):
        self.items.insert(0,item)

    def avanzar(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


