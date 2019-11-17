def miesci(x,y,z):
    int(x)
    int(y)
    int(z)
    if x>=y and x<=z:
        return 1
    else:
        return 0
      
x=input('Podaj liczbę: ')
print('Podaj zakres <x,y>: ')
y=input('x=')
z=input('y=')

if miesci(x,y,z)==1:
    print('Liczba {} mieści się w przedziale <{},{}>.'.format(x,y,z))
else:
    print('Liczba {} nie mieści się w przedziale <{},{}>.'.format(x,y,z))