import heapq

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, priority, data):
        heapq.heappush(self.queue, (priority, data))

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Empty Queue")
        else:
            return heapq.heappop(self.queue)[1]
        
    def peek(self):
        if self.isEmpty():
            raise IndexError("Empty Queue")
        else:
            return self.queue[0][1]
        
    def isEmpty(self):
        return len(self.queue) == 0
    
q = Queue()
q.enqueue(2, "Moriah")
q.enqueue(1, "Hannah")
q.enqueue(3, "Manuel")

print(q.dequeue())
print(q.peek())