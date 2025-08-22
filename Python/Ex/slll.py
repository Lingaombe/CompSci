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
        if self.head:
            new.next = self.head
            self.head = new
        else:
            self.head = new
            self.tail = new

    def append(self, data):
        new = Node(data)
        if self.tail:
            self.tail.next = new
            self.tail = new
        else:
            self.tail = new
            self.head = new

    def search(self, data):
        temp = self.head
        while temp:
            if temp.data == data:
                return True
            temp = temp.next
        return False
        
    def delete(self):
        if self.head:
            temp = self.head
            self.head = self.head.next
            del temp
        else:
            print("delete from empty list")

    def deletev(self, value):
        temp = self.head
        if temp.data == value:
            self.head = temp.next
            return
        while temp:
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
sll.append(30)
sll.prepend(40)
sll.append(10)

sll.traverse()
print(sll.search(80))
sll.delete()
sll.traverse()
sll.deletev(10)
sll.traverse()
sll.deletev(20)
sll.traverse()