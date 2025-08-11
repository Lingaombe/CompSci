class Node:
    def __init__(self, c, p):
        self.p = p
        self.c = c
        self.next = None
        self.head = None

    def Add(poly1, poly2):
        result = Node(0, 0)
        current = result

        while poly1 and poly2:
            if poly1.p > poly2.p:
                current.next = Node(poly1.c, poly1.p)
                poly1 = poly1.next
            
            elif poly1.p < poly2.p:
                current.next = Node(poly2.c, poly2.p)
                poly2 = poly2.next

            else:
                Csum = poly1.c+poly2.c
                if Csum != 0:
                    current.next = Node(poly1.c, poly1.p)
                    current = current.next
                poly1 = poly1.next
                poly2 = poly2.next
                continue
            current = current.next
        
        while poly1:
            current.next = Node(poly1.c, poly1.p)
            poly1 = poly1.next
            current = current.next

        while poly2:
            current.next = Node(poly2.c, poly2.p)
            poly2 = poly2.next
            current = current.next

        return result.next
    
    def Multi(poly1, poly2):
        result = Node(1, 1)
        current = result


    def Print(poly):
        while poly:
            print(f'{poly.c}x^{poly.p}', end=" ")
            if poly.next:
                print("+", end=" ")
            poly = poly.next
        print()

poly1 = Node(3,3)
poly1.next = Node(2, 1)
poly1.next.next = Node(3,0)

poly2 = Node(2,2)
poly2.next = Node(3, 1)
poly2.next.next = Node(4,0)

poly2.Print()
poly1.Print()

res = poly1.Add(poly2)
res.Print()