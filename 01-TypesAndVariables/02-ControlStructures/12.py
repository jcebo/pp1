x=int(input("Wprowadz liczbe calkowita x: "))
y=int(input("Wprowadz liczbe calkowita y: "))
if (x<0 and y<0):
    print('obie liczby sa ujemne')
elif (x<0 and y>=0):
    print('tylko x jest ujemne')
elif (x>=0 and y<0):
    print('tylko y jest ujemne')
elif (x>0 and y>0):
    print('obie liczby sa dodatnie')