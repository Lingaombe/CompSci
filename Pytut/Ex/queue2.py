class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        return self.queue.pop(0)
    
    def peek(self):
        return self.queue[0]
    

qu = Queue()
qu.enqueue(10)
qu.enqueue(20)
qu.enqueue(30)
print(qu.dequeue())
print(qu.peek())