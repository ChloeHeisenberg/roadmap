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

# Insert a new node after an existing node

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception('List is empty')
        
        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return
        
        raise Exception("Node with data '%s' not found" % target_node_data)
    
    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception('List is empty')
        
        if self.head.data == target_node_data:
            return self.add_first(new_node)
        
        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)
    
    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception('List is empty')
        
        if self.head.data == target_node_data:
            self.head = self.head.next
            return
        
        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

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

# Exception: List is empty
# llist = LinkedList()
# llist.add_after('a', Node('b'))

llist = LinkedList(['a', 'b', 'c', 'd'])
print(llist)

llist.add_after('c', Node('cc'))
print(llist)

#Exception: Node with data 'f' not found
# llist.add_after('f', Node('g'))

#Exception: List is empty
# llist = LinkedList()
# llist.add_before('a', Node('a'))

llist = LinkedList(['b', 'c'])
print(llist)

llist.add_before('b', Node('a'))
print(llist)

llist.add_before('b', Node('aa'))
llist.add_before('c', Node('bb'))
print(llist)

# Exception: Node with data 'n' not found
# llist.add_before('n', Node('m'))

# Exception: List is empty
# llist = LinkedList()
# llist.remove_node('a')

llist = LinkedList(['a', 'b', 'c', 'd', 'e'])
print(llist)

llist.remove_node('a')
print(llist)

llist.remove_node('e')
print(llist)

llist.remove_node('c')
print(llist)

# Exception: Node with data 'a' not found
# llist.remove_node('a')