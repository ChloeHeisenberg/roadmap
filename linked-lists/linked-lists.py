# Linked Lists in Python Tutorial

from collections import deque

# Create a class to represent each node of the linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data
    
# Create class that represents a linked list
    
class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next


    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append('None')
        return ' -> '.join(nodes)
    
# Traverse a linked list
    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

# Insert a new node

    def add_first(self, node):
        node.next = self.head
        self.head = node

# Insert a new node at the end

    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node
    
llist = LinkedList()
print(llist)

first_node = Node('a')
llist.head = first_node
print(llist)

second_node = Node('b')
third_node = Node('c')
first_node.next = second_node
second_node.next = third_node
print(llist)

llist = LinkedList(['a', 'b', 'c', 'd', 'e'])
print(llist)

for node in llist:
    print(node)

llist = LinkedList()
print(llist)

llist.add_first(Node('b'))
print(llist)

llist.add_first(Node('a'))
print(llist)

llist = LinkedList(['a', 'b', 'c', 'd'])
print(llist)

llist.add_last(Node('e'))
print(llist)

llist.add_last(Node('f'))
print(llist)