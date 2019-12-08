class kostka():
    def __init__(self):
        self.oczka=0
    def rzuc(self):
        import random
        self.oczka=random.randrange(1,7)
        return self.oczka
k1=kostka()
k2=kostka()
k3=kostka()
suma = 0
n=1
while n<=4:
    print(f'K1: {k1.rzuc()} K2: {k2.rzuc()} K3: { k3.rzuc()}\nSuma = {k1.oczka+k2.oczka+k3.oczka}')
    n+=1
    
   