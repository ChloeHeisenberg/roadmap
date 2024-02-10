class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, prev_node, new_data):

        if prev_node is None:
            print('The given previous node must inLinkedList.')
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def insertAtEnd(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        while (last.next):
            last = last.next
        
        last.next = new_node

    def deleteNode(self, position):

        if self.head is None:
            return
        
        temp = self.head
        if position == 0:
            self.head = temp.next
            temp = None
            return
        
        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break

        if temp is None:
            return
        
        if temp.next is None:
            return
        
        next = temp.next.next
        temp.next = None
        temp.next = next

    def search(self, key):

        current = self.head

        while current is not None:
            if current.data == key:
                return True
            current = current.next
        return False
    
    def sortLinkedList(self, head):
        current = head
        index = Node(None)

        if head is None:
            return
        else:
            while current is not None:
                index = current.next

                while index is not None:
                    if current.data > index.data:
                        current.data, index.data = index.data, current.data

                    index = index.next
                current = current.next

    def printLinkedList(self):
        temp = self.head
        while (temp):
            print(str(temp.data) + " ", end="")
            temp = temp.next

if __name__ == '__main__':

    llist = LinkedList()
    llist.insertAtEnd(5)
    llist.insertAtBeginning(8)
    llist.insertAtBeginning(4)
    llist.insertAtEnd(6)
    llist.insertAfter(llist.head.next, 9)

    print("My linked list: ")
    llist.printLinkedList()

    print('\nAfter deleting en element:')
    llist.deleteNode(4)
    llist.printLinkedList()

    print()
    item = 8
    if llist.search(item):
        print(str(item) + ' is found.')
    else:
        print(str(item) + ' is not found.')

    llist.sortLinkedList(llist.head)
    print('My sorted list: ')
    llist.printLinkedList()