class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 0:
            return None
        return self.queue.pop(0)
    
    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)
    
q = Queue()
q.enqueue(1)
q.enqueue(8)
q.display()
print(q.size())
q.enqueue(4)
q.enqueue(3)
q.enqueue(8)
print('Queue: ')
q.display()
q.dequeue()
print('Now Queue: ')
q.display()
print(q.size())