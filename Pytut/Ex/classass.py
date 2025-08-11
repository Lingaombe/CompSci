class item:
    @staticmethod
    def calculate_area(radius,pi=3.14):
        return f'area is {(radius**2)*pi}'

    
print(item.calculate_area(10))