class books:
    pay_rate = 0.8

    avail_books = []
    def __init__(self, name: str, author: str, price: int, quantity: int):
        assert price >= 0, f"Price {price} is less than 0"
        assert quantity >= 0, f"Quantity {quantity} is less than 0"
        self.name = name
        self.author  = author
        self.price = price
        self.quantity = quantity
    
        books.avail_books.append(self.name)

book1 = books("OSTG", "Hannah", 700, 3)
book2 = books("ACAR", "Hannah", 800, 3)
book3 = books("Breathe", "Hannah", 500, 5)

print(book1.name)
print(books.avail_books)
print(books.__dict__)