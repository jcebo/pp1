class bank_account():
    def __init__(self,no):
        self.no = no
        self.balance = 0
    def topup(self,amount):
        self.balance += amount
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance -= amount
        else:
            print('Niewystarczająca ilość środków')
    def status(self):
        print(f'Numer rachunku: {self.no}\nSaldo: {self.balance} zł') 
        
a = bank_account("12 3456 5555 9090 1111 0000 7722")
a.status()
a.topup(25.30)
a.status()
a.withdraw(31.70)
a.status()
a.withdraw(14)
a.status()