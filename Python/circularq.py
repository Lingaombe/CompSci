class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None]*capacity
        self.size = 0
        self.front = 0
        self.rear = 0

    def enqueue(self, data):
        if self.size >= self.capacity:
            raise IndexError("Queue is full")
        self.queue[self.rear] = data
        self.rear = (self.rear + 1)%self.capacity
        self.size +=1

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Queue is empty")
        data = self.queue[self.front]
        self.front = (self.front + 1)%self.capacity
        self.size -=1
        return data
    
    def peek(self):
        if self.isEmpty():
            raise IndexError("Queue is empty")
        return self.queue[self.front]
    
    def isEmpty(self):
        return self.size == 0
    
c = Queue(4)

c.enqueue(1)
c.enqueue(9)
print(c.dequeue())