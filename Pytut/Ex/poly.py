class Node:
    def __init__(self, c, p):
        self.c = c
        self.p = p
        self.next = None

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
                c = poly1.c+poly2.c
                if c != 0:
                    current.next = Node(c, poly2.p)
                poly1 = poly1.next
                poly2 = poly2.next
            current = current.next

        while poly1:
            current.next = Node(poly2.c, poly2.p)
            poly1 = poly1.next
            current = current.next
        while poly2:
            current.next = Node(poly2.c, poly2.p)
            poly2 = poly2.next
            current = current.next
        return result.next
    
    def Print(poly):
        while poly:
            print("{}x^{}". format(poly.c, poly.p), end="")
            if poly.next:
                print("+", end="")
            poly = poly.next
        print()

poly1 = Node(3, 2) 
poly1.next = Node(2, 1) 
poly1.next.next = Node(1, 0) 

poly2 = Node(2, 3) 
poly2.next = Node(1, 1) 
poly2.next.next = Node(5, 0) 

print("Polynomial 1:") 
poly1.Print() 
print("Polynomial 2:") 
poly2.Print() 
result = poly1.Add(poly2) 
print("Sum of the two polynomials:") 
result.Print()