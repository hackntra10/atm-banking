from atm_card import ATMCard 

class Customer:
    def __init__(self, id, custPin=1234, custBalance = 10000):
        self.id = id
        self.custPin = custPin 
        self.custBalance = custBalance 
    
    def showId(self):
        return self.id 
    
    def showPin(self):
        return self.custPin 

    def showBalance(self):
        return self.custBalance 
    
    def debetCust(self, nominal):
        self.custBalance -= nominal
       

    def simpanCust(self, nominal):
        self.custBalance += nominal
    