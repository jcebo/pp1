class Plane:
    def __init__(self,no):
        self.no = no
        self.high = 0
    def start(self,high):
        if high>1000 and high<2000:
            self.high = high
        else:
            print('Wymagana wysokość jest nieprawidłowa.')
    def change(self,high):
        if high in range(300,11001):
            self.high = high
        else:
            print('Uwaga, wysokość, którą chcesz osiągnąć jest niebezpieczna!')
    def landing(self):
        if self.high<500:
            self.high = 0
        else:
            print('Zbyt duża wysokość dla lądowania. Obniż lot.')
    def status(self):
        print(f'Tu {self.no}, moja wysokość lotu to {self.high} m.')

samolot = Plane('LOT881')
samolot.start(1500)
samolot.status()
samolot.change(8900)
samolot.status()
samolot.change(200)
samolot.status()
samolot.landing()
samolot.change(400)
samolot.landing()
samolot.status()