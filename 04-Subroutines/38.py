def wielkie(ciag):
    wynik=[]
    for x in ciag:
        if ord(x)>64 and ord(x)<91:
            wynik.append(x)
    return wynik
u=input('Podaj ciąg liter: ')
a=wielkie(u)
for x in a:
    print(x,end='')