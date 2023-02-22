class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        # create new Node
        # add Node to the end
        pass

    def prepend(self, value):
        # create new Node
        # add Node to the begining
        pass

    def insert(self, index, value):
        # create new Node
        # insert Node
        pass
