class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, data):
        self.stack.append(data)
        self.size +=1

    def pop(self):
        if self.isEmpty():
            raise IndexError("Pop from stack")
        else:
            self.size -=1
            return self.stack.pop()
        
    def peek(self):
        if self.isEmpty():
            raise IndexError("Pop from stack")
        else:
            return self.stack[-1]
        
    def Size(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0
    
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
print(stack.Size())
print(stack.pop())
print(stack.peek())