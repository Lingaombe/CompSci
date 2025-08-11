class Queue:
    def __init__(self):
        self.queue = []
        self.size = 0

    def enqueue(self, data):
        self.queue.append(data)
        self.size +=1

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Dequeue from empty queue")
        else:
            self.size -=1
            return self.queue.pop(0)
        
    def peek(self):
        if self.isEmpty():
            raise IndexError("Dequeue from empty queue")
        else:
            return self.queue[0]
        
    def Size(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0
    

queue = Queue()
queue.enqueue(10)
queue.enqueue(12)
queue.enqueue(14)
print(queue.dequeue())
print(queue.peek())