class cola():
    def __init__(self, size):
        self.list = []
        self.size = size
        self.last = -1

    def IsEmpty(self):
        if self.last == -1:
            return True
        else:
            return False

    def IsFull(self):
        if self.size == self.last+1:
            return True
        else:
            return False

    def Enqueue(self, value):
        if not self.IsFull():
            self.list.append(value)
            self.last+=1

    def Dequeue(self):
        if not self.IsEmpty():
            self.list.pop(0)
            self.last-=1

    def getLast(self):
        if not self.IsEmpty():
            return self.list[-1]
        else:
            return False

    def getFirst(self):
        if not self.IsEmpty():
            return self.list[0]