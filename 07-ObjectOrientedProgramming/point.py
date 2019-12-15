from math import sqrt
class Point():
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'P({self.x},{self.y})'
    def __eq__(self, other):
        if isinstance(other, Point):
            if other.x==self.x and other.y==self.y:
                return 'Odległość pomiędzy punktami wynosi 0'
            else:
                return f'Odległość między punktami to: {sqrt((other.x-self.x)**2+(other.y-self.y)**2)} ' 
        else:
            return False
