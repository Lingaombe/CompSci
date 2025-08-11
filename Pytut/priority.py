import heapq

class Customer:
    def __init__(self, n, p):
        self.p = p
        self.n = n
    
    def __lt__(self, o):
        self.p < o.p


class Tickets:
    def __init__(self):
        self.qq = []

    def addc(self, customer):
        heapq.heappush(self.qq, customer)

    def servec(self):
        cus = heapq.heappop(self.qq)
        return cus.n
    
list = Tickets()
list.addc(Customer("Hannah", 1))
list.addc(Customer("Emmanuel", 3))
list.addc(Customer("Moriah", 2))

print(list.servec())   