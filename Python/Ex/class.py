import csv


class item:
    #class attributes are given to all objects within a class
    pay_rate = 0.8
    all = []
    #init executes upon object creation
    #a method is just a function passed in class
    def __init__(self, name: str, price: float, quantity: int):

        #make sure passed argument is valid
        assert price >= 0, f"Price {price} is negative"
        assert quantity >= 0, f"Quantity {quantity} is negative"

        #make sure every object has these attributes
        self.name = name
        self.price = price
        self.quantity = quantity

        item.all.append(self)

    def calc_total_price(self):
        return f"Price before discount: {self.price * self.quantity}"
    def apply_discount(self):
            self.price = self.price * self.pay_rate
            return f"Price after discount: {self.price * self.quantity}"
    
    #representing your objects method
    def __repr__(self):
         return f"Item: '{self.name}', {self.price}, {self.quantity}"
    
    @classmethod 
    def instantiate_from_csv(cls):
           with open('class.csv','r') as f:
                reader = csv.DictReader(f)
                items = list(reader)
            
           for i in items:
                print(i)

item.instantiate_from_csv()





#csv comma separated values
# __dict__ shows all attributes belonging to object or class, returns a dictionary data type
#print(item1.__dict__)