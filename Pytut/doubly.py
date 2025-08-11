class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def prepend(self, data):
        new = Node(data)
        self.size +=1
        if not self.head:
            self.head = new
            self.tail = new
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new

    def append(self, data):
        new = Node(data)
        self.size +=1
        if not self.tail:
            self.tail = new
            self.head = new
        else:
            new.prev = self.tail
            self.tail.next = new
            self.tail = new

    def insert(self, data, index):
        temp = self.head
        if index == 0:
            self.prepend(data)

        elif index-1 >= self.size:
            self.append(data)

        else:
            c = 0
            while temp:
                c+=1
                if index == c:
                    new = Node(data)
                    new.prev = temp.prev
                    new.next = temp
                    if temp.prev:
                        temp.prev.next = new
                    else:
                        self.head = new
                    temp.prev = new
                    return
                temp = temp.next
            
    def deleteatbeg(self):
        if not self.head:
            raise IndexError("List is Empty")
        else:
            self.size -=1
            self.head = self.head.next

    def deleteatend(self):
        if not self.head:
            raise IndexError("List is Empty")
        else:
            self.size -=1
            temp = self.tail
            self.tail = self.tail.prev
            del temp

    def delete(self, value):
        temp = self.head
        if temp.data == value:
            self.head = self.head.next
            if self.head.prev:
                self.head.prev = None
        while temp and temp.next:
            temp = temp.next
            if temp.data == value:
                if temp.prev:
                    temp.prev.next = temp.next
                temp.next.prev = temp.prev

    def search(self, value):
        temp = self.head
        while temp:
            if temp.data == value:
                return True
            temp = temp.next
        return False

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end="<->")
            temp = temp.next
        print("None")

list = DLL()
list.prepend(10)
list.append(1)
list.append(2)
list.append(5)
print(list.search(1))
print(list.search(11))
list.delete(1)
list.traverse()