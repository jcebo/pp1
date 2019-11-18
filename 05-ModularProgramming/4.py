import math
x=float(3.7)
y=4
sqrtX=math.sqrt(x)
power=math.pow(x,y)
c=math.pow(x,1/y)
pi=math.pi
polekola=math.pow(y,2)*pi
silnia=math.factorial(y)
f=math.floor(x)

print(f"Pierwiastek kwadratowy z {x} wynosi {sqrtX}, x do potęgi y to {power}", end=' ')
print(f' Pierwiastek y-tego stopnia z x to {c}, Pole koła o promieniu y to {polekola}, silnia y to {silnia}, Największą możliwą liczbę całkowitą, mniejszą bądź równą x to {f}')