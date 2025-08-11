class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SortedLL:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new = Node(data)
        if not self.head or self.head.data >= data:
            new.next = self.head
            self.head = new
        else:
            temp = self.head
            while temp.next and temp.next.data < data:
                temp = temp.next
            new.next = temp.next
            temp.next = new            
                
    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("None")

sl = SortedLL()
sl.insert(10)
sl.insert(1)
sl.insert(20)
sl.traverse()