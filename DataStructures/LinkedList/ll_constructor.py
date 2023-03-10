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
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    # def prepend(self, value):
    #     new_node = Node(value)

    # def insert(self, index, value):
    #     # create new Node
    #     # insert Node
    #     pass

    def pop(self):

        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while (temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head == None
            self.tail == None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        popValue = self.head
        self.head = self.head.next
        popValue.next = None
        self.length -= 1
        if self.length == 0:
            self.tail == None
        return popValue

    def get(self, index):
        if self.length <= index or index < 0:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, value, index):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        new_node = Node(value)
        if index > self.length or index < 0:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index >= self.length or index < 0:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index-1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    # def reverseList(self):
    #     currentNode = self.head
    #     prevNode = ''
    #     nextNode = ''
    #     for _ in range(self.length):

    #         if currentNode == self.head:
    #             nextNode = currentNode.next
    #             currentNode.next = None
    #             prevNode = currentNode
    #             currentNode = nextNode
    #         elif currentNode == self.tail:
    #             currentNode.next = prevNode
    #             self.head = self.tail
    #             currentNode = self.head
    #             return
    #         else:
    #             nextNode = currentNode.next
    #             currentNode.next = prevNode
    #             prevNode = currentNode
    #             currentNode = nextNode
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
