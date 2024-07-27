# Definition of linked list
# A linked list is a linear data structure where each element is a separate object. 
# Each element (we will call it a node) of a list is comprising of two items - the data and a reference to the next node. The last node has a reference to null.
# The entry point into a linked list is called the head of the list.By traversing the list from head to the end, we can access each node.

def linked_list():
    class Node:
        def __init__(self, data): # WHAT IS THIS?
            # Constructor to initialize the node object
            
            # The data is passed to the node
            self.data = data
            # Next is initialized as null
            self.next = None

    class LinkedList:
        def __init__(self):
            self.head = None

        def append(self, data):
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
                return
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node
            
        def delete(self, key):
            current = self.head
            if current and current.data == key:
                self.head = current.next
                current = None
                return
            prev = None
            while current and current.data != key:
                prev = current
                current = current.next
            if current is None:
                return
            prev.next = current.next
            current = None

        def print_list(self):
            current = self.head
            while current:
                print(current.data)
                current = current.next

    # Test the function
    llist = LinkedList()
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.append(4)
    llist.print_list()
    
linked_list() # 1 2 3 4
    
