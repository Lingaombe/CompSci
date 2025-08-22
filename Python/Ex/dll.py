class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DLL:
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
            self.head.prev = new
            self.head = new
    
    def insert(self, data):
        new = Node(data)
        if not self.tail:
            self.head = new
            self.tail = new
        else:
            new.prev = self.tail
            self.tail.next = new
            self.tail = new

    def delhead(self):
        if not self.head:
            print("Delete from empty list")
        else:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            del temp

    def deltail(self):
        if not self.tail:
            print("Delete from empty list")
        else:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            del temp
        
    def search(self, value):
        if not self.head:
            print("Search from empty list")
        else:
            temp = self.head
            while temp:
                if temp.data == value:
                    return True
                temp = temp.next
            return False

    def insertafternode(self, data, value):
        temp = self.head
        while temp:
            if temp.data == value:
                new = Node(data)
                new.next = temp.next
                new.prev = temp
                if temp.next:
                    temp.next.prev = new
                temp.next = new
            temp = temp.next

    def insertbeforenode(self, data, value):
        temp = self.head
        while temp:
            if temp.data == value:
                new = Node(data)
                new.prev = temp.prev
                new.next = temp
                if temp.prev:
                    temp.prev.next = new
                else:
                    self.head = new
                temp.prev = new
            temp = temp.next

    def remove(self, value):
        if self.head.data == value:
            temp = self.head
            self.head = self.head.next
            self.head.next.prev = None
            del temp
        temp = self.head
        while temp:
            if temp.data == value:
                temp.next = temp.next.next
                return
            temp = temp.next

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end="<->")
            temp = temp.next
        print("None")

    def reverse(self):
        temp = self.tail
        while temp:
            print(temp.data, end="<->")
            temp = temp.prev
        print("None")

dll = DLL()
dll.prepend(20)
dll.insert(10)
dll.insert(30)
dll.prepend(40)
dll.traverse()
dll.reverse()
dll.delhead()
dll.traverse()
dll.deltail()
dll.traverse()

print(dll.search(10))
dll.prepend(40)
dll.insertbeforenode(70,20)
dll.traverse()
dll.insertafternode(60,10)
dll.traverse()
print()
dll.remove(10)
dll.traverse()