class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0

    def enqueue(self, data):
        self.size +=1
        new = Node(data)
        if not self.tail:
            self.tail = new
            self.head = new
        else:
            self.tail.next = new
            self.tail = new

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Queue is empty")
        else:
            self.size -=1
            temp = self.head
            self.head = self.head.next
            return temp.data
        
    def peek(self):
        if self.isEmpty():
            raise IndexError("Queue is empty")
        else:
            return self.head.data
        
    def Size(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0
    
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(queue.Size())
print(queue.dequeue())
print(queue.peek())
print(queue.isEmpty())