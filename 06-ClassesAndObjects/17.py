import math
class ulamek():
    def __init__(self,licznik,mianownik):
        self.licznik=licznik
        self.mianownik=mianownik
        self.dzielnik=0
    def show(self):
        print(f'{self.licznik}/{self.mianownik}')
    def simplify(self):
        self.dzielnik=math.gcd(self.licznik,self.mianownik)
        self.licznik/=self.dzielnik
        self.mianownik/=self.dzielnik
        self.licznik=int(self.licznik)
        self.mianownik=int(self.mianownik)
ul=ulamek(1,2)
ul.simplify()
ul.show()
ul2=ulamek(12,21)
ul2.show()
ul2.simplify()
ul2.show()