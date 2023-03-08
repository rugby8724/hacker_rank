class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def stack_push(self, value):
        new_node = Node(value)
        if self.top == None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True

    def stack_pop(self, value):
        if self.top == None:
            return False
        popped = self.top
        if self.height == 1:
            self.top = None
        else:
            self.top = popped.next
            popped.next = None
        self.height -= 1
        return popped
