class Node: 
    def __init__(self, c, p): 
        self.c = c  
        self.p = p  
        self.next = None  
    def add_polynomials(poly1, poly2): 
        result = Node(0, 0) 
        current = result 
 
        while poly1 is not None and poly2 is not None: 
            if poly1.p > poly2.p: 
                current.next = Node(poly1.c, poly1.p) 
                poly1 = poly1.next 
            elif poly1.p < poly2.p: 
                current.next = Node(poly2.c, poly2.p) 
                poly2 = poly2.next 
            else:  
                c_sum = poly1.c + poly2.c 
                if c_sum != 0: 
                    current.next = Node(c_sum, poly1.p) 
                    current = current.next 
                poly1 = poly1.next 
                poly2 = poly2.next 
                continue 
            current = current.next 
            
        while poly1 is not None: 
                current.next = Node(poly1.c, poly1.p) 
                poly1 = poly1.next 
                current = current.next 
 
        while poly2 is not None: 
                current.next = Node(poly2.c, poly2.p) 
                poly2 = poly2.next 
                current = current.next 
        return result.next  
 
    def print_polynomial(poly): 
        while poly is not None: 
            print(f"{poly.c}x^{poly.p}", end=" ") 
            if poly.next is not None: 
                print("+", end=" ") 
            poly = poly.next 
        print() 
 
poly1 = Node(5, 4) 
poly1.next = Node(3, 2) 
poly1.next.next = Node(2, 1) 
poly1.next.next.next = Node(1, 0) 
# Create polynomial 2: 3x^3 + 2x^2 + x + 5 
poly2 = Node(9, 5) 
poly2.next = Node(2, 3) 
poly2.next.next = Node(1, 1) 
poly2.next.next.next = Node(5, 0) 
 
 
result = poly1.add_polynomials(poly2) 
print("Sum of the two polynomials:") 
result.print_polynomial() 
 
