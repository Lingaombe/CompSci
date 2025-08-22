import heapq

class Priority:
    def __init__(self):
        self.queue = []

    def addc(self, priority, name):
        heapq.heappush(self.queue, (name, priority))

    def servec(self):
        return heapq.heappop(self.queue)[1]

list = Priority()
list.addc("Hannah", 1)
list.addc("Emmanuel", 3)
list.addc("Moriah", 2)

print(list.servec())