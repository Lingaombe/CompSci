class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.isEmpty():
            raise IndexError("Pop from empty stack")
        else:
            return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            raise IndexError("Peek from empty stack")
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)
    
    def isEmpty(self):
        return self.size() == 0
    
    def Print(self):
        for i in self.stack:
            print(i, end="-")
        print()
    
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.Print()
print(stack.peek())
print(stack.pop())
print(stack.peek())