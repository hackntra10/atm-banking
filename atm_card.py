class ATMCard:
    def __init__(self, defaultPin, defaultBalance):
        self.defaultPin = defaultPin
        self.defaultBalance = defaultBalance
    
    def showPin(self):
        return self.defaultPin 
    
    def showBalance(self):
        return self.defaultBalance

