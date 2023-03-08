class Node:
    def _init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node

        self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.head == None:
            return None
        popped = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        popped.prev = None
        self.length -= 1
        return popped

    def prepend(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.head == None:
            return False
        popped = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = popped.next
            self.head.prev = None
        popped.next = None
        self.length -= 1
        return popped

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def dll_insert(self, index, value):

        temp = self.get(index)
        if temp:
            if index == 0:
                return self.prepend(value)
            if index == self.length:
                return self.append(value)
            new_node = Node(value)
            new_node.prev = temp.prev
            temp.prev = new_node
            new_node.next = temp
            self.length += 1
            return True
        return False

    def dll_remove(self, index):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            self.pop_first()
        elif index == self.length - 1:
            self.pop()
        else:
            temp = self.get(index)
            pre = self.get(index - 1)
            post = self.get(index+1)
            pre.next = temp.next
            post.prev = temp.prev
            temp.prev = None
            temp.next = None
            self.length -= 1
        return True
