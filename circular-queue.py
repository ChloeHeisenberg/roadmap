class MyCircleQueue:

    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    def enqueue(self, data):
        
        if ((self.tail + 1) % self.k == self.head):
            print('My circle queue is full.\n')
        
        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data

        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = data

    def dequeue(self):

        if (self.head == -1):
            print('My circle queue is empty.\n')

        elif (self.tail == self.head):
            temp = self.queue[self.head]
            self.tail = -1
            self.tail = -1
            return temp
        
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.k
            return temp
        
    def PrintCQueue(self):

        if (self.head == -1):
            print('My circular queue has no items.\n')

        elif (self.tail >= self.head):
            for i in range(self.head, self.tail+1):
                print(self.queue[i], end=" ")
            print()

        else:
            for i in range(self.head, self.k):
                print(self.queue[i], end=" ")
            for i in range(0, self.tail+1):
                print(self.queue, end=" ")
            print()

myq = MyCircleQueue(6)
myq.enqueue(4)
myq.enqueue(2)
myq.enqueue(8)
myq.enqueue(5)
myq.PrintCQueue()
myq.enqueue(7)
myq.enqueue(1)
myq.PrintCQueue()
myq.dequeue()
myq.PrintCQueue()