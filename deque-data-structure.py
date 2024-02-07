class Deque:

    def __init__(self):
        self.items = []

    def checkEmpty(self):
        return self.items == []
    
    def addFront(self, item):
        self.items.insert(0, item)

    def addRear(self, item):
        self.items.append(item)

    def removeFront(self, item):
        return self.items.pop(0)
    
    def removeRear(self, item):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    def printDeque(self):
        myDeque = []
        for i in self.items:
            myDeque.append(i)
        return myDeque
    
d = Deque()
print(d.checkEmpty())
d.addFront(0)
d.addFront(7)
d.addFront(3)
print('My deque is this big - ', d.size())
d.addRear(4)
d.addRear(1)
d.addRear(5)
print('Now my deque is this big - ', d.size())
print('My deque: ', d.printDeque())
d.removeFront(3)
d.removeRear(5)
print('After removing the items from the front and rear my deque is this big - ', d.size())
print('My deque: ', d.printDeque())