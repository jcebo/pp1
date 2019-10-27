import math
a=float(input("Podaj bok a: "))
b=float(input("Podaj bok b: "))
c=float(input("Podaj bok c: "))
p=0.5*(a+b+c)
h=math.sqrt(p*(p-a)*(p-b)*(p-c))

print(f'Pole trojkata to {h}')