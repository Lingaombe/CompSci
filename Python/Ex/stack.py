class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, data):
        new = Node(data)
        if not self.head:
            self.head = new
        new.next = self.head
        self.head = new
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise IndexError("Empty stack")
        else:
            temp = self.head
            self.head = self.head.next
            return temp.data
        
    def peek(self):
        if self.isEmpty():
            raise IndexError("Empty stack")
        else:
            return self.head.data
        
    def isEmpty(self):
        return self.size == 0
    
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.pop())
print(stack.peek())