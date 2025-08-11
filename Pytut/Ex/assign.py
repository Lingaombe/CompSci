import heapq 
 
class Customer: 
    def __init__(self, name, priority): 
        self.name = name 
        self.priority = priority 
 
    def __lt__(self, other): 
        return self.priority < other.priority 
 
class AirlineTicketCounter:
    def __init__(self): 
        self.pq = [] 
     
    def add_customer(self, Customer): 
        heapq.heappush(self.pq, Customer) 
     
    def serve_customer(self): 
        if self.pq is None: 
            raise IndexError("No customers to serve") 
        customer = heapq.heappop(self.pq) 
        return customer.name 

    def display(self):
        if not self.pq:
            print("Priority Queue is empty")
        else:
            print("Priority Queue:")
            for item in self.pq:
                print(f"Name: {item.name} Priority: {item.priority}")

counter = AirlineTicketCounter() 
counter.add_customer(Customer("John", 2))  # priority 2 
counter.add_customer(Customer("Alice", 1))  # priority 1 
counter.add_customer(Customer("Bob", 3))    # priority 3 
counter.display()
print(counter.serve_customer())  # Output: Alice 
print(counter.serve_customer())  # Output: John 
