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
        self.size +=1
        if not self.head:
            self.head = new
        else:
            new.next = self.head
            self.head = new

    def pop(self):
        if self.isEmpty():
            raise IndexError("Empty Stack")
        else:
            temp = self.head
            self.size -=1
            self.head = self.head.next
            return temp.data
        
    def peek(self):
        if self.isEmpty():
            raise IndexError("Empty Stack")
        else:
            return self.head.data
        
    def Size(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0
    
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.pop())
print(stack.peek())
print(stack.Size())