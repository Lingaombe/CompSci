class BankAccount: 
    def __init__(self, account_number, balance): 
        self.__account_number = account_number 
        self.__balance = balance

class In(BankAccount):
    def __init__(self,account_number, balance):
        super().__init__(account_number,balance) 

    def display_balance(self): 
        print("Balance:", self.__balance) 
        
b = In(1234567890, 5000) 
b.display_balance() 