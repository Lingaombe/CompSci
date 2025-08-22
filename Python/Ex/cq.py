class CQ:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.size = 0
        self.head = 0
        self.tail = 0

    def enqueue(self, data):
        self.queue[self.tail] = data
        self.tail = (self.tail + 1)%self.capacity
        self.size += 1

    def dequeue(self):
        data = self.queue[self.head]
        self.head = (self.head + 1)%self.capacity
        self.size -= 1
        return data