import gc

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def insertFront(self, data):

        new_node = Node(data)

        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

    def insertAfter(self, prev_node, data):

        if prev_node is None:
            print('Previous node cannot be null')
            return

        new_node = Node(data)

        new_node.next = prev_node.next

        prev_node.next = new_node

        new_node.prev = prev_node

        if new_node.next:
            new_node.next.prev = new_node

    def insertEnd(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node

        new_node.prev = temp
        return
    
    def deleteNode(self, deleteNode):

        if self.head is None or deleteNode is None:
            return
        
        if self.head == deleteNode:
            self.head = deleteNode.next

        if deleteNode.next is not None:
            deleteNode.next.prev = deleteNode.prev

        if deleteNode.prev is not None:
            deleteNode.prev.next = deleteNode.next

        gc.collect()

    def printDLinkedList(self, node):

        while node:
            print(node.data, end='->')
            node = node.next

DlinkedList = DoublyLinkedList()

DlinkedList.insertEnd(3)
DlinkedList.insertFront(2)
DlinkedList.insertFront(7)
DlinkedList.insertEnd(4)
print('My doubly linked list:')
DlinkedList.printDLinkedList(DlinkedList.head)
DlinkedList.insertAfter(DlinkedList.head, 5)
DlinkedList.insertAfter(DlinkedList.head.next, 6)
print('\nAfter the insertion my doubly linked list looks line this:')
DlinkedList.printDLinkedList(DlinkedList.head)
DlinkedList.deleteNode(DlinkedList.head.next.next)
print('\nAfter deletion my doubly linked list looks line this:')
DlinkedList.printDLinkedList(DlinkedList.head)