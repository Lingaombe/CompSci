
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertatend(self, data):
        newnode = Node(data)

        if self.tail:
            self.tail.next = newnode
        self.tail = newnode
        if not self.head:
            self.head = newnode

    def insertattop(self, data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

    def trasverse(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next

    def search(self, value):
        if not self.head:
            print("empty list")
        else:
            current = self.head
            while current:
                if current.data == value:
                    return True
                current = current.next
            return False
    


listed = SLL()
listed.insertatend(10)

listed.insertatend(20)

listed.insertattop(30)


listed.trasverse()

if listed.search(40) == True:
    print("\nFound")
else:
    print("\nNot Found")

