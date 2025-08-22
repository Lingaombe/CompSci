class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self, data):
        new = Node(data)
        if not self.head:
            self.head = new
            self.tail = new
        else:
            new.next = self.head
            self.head = new

    def append(self, data):
        new = Node(data)
        if not self.tail:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            self.tail = new

    def search(self, value):
        temp = self.head
        while temp:
            if temp.data == value:
                return True
            temp = temp.next
        return False
    
    def delete(self, value):
        if not self.head:
            raise IndexError("List is empty")
        else:
            temp = self.head
            if temp.data == value:
                self.head = self.head.next
            while temp and temp.next:
                if temp.next.data == value:
                    temp.next = temp.next.next
                    return
                temp = temp.next

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("None")

sll = SLL()
sll.prepend(20)
sll.prepend(30)
sll.delete(30)
sll.traverse()