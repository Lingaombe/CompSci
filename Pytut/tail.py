class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class SLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new = Node(data)
        if not self.tail:
            self.tail = new
            self.head = new

        else:
            self.tail.next = new
            new.prev = self.tail
            self.tail = new

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("None")

    def reverse(self):
        temp = self.tail
        while temp:
            print(temp.data, end="<->")
            temp = temp.prev
        print("Head")


sll = SLL()

sll.append(20)
sll.append(30)
sll.traverse()
sll.reverse()