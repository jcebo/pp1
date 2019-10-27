liczba=int(input("Wprowadz liczbe calkowita: "))
if (liczba>0 and liczba%2!=0):
    print('Ta liczba jest dodatnia i nieparzysta')
elif (liczba>0 and liczba%2==0):
    print('ta liczba jest dodatnia i parzysta')
elif (liczba==0):
    print('ta liczba to 0')
elif (liczba<0 and liczba%2==0):
    print('ta liczba jest ujemna i parzysta')
elif (liczba<0 and liczba%2!=0):
    print('ta liczba jest ujemna i nieparzysta')
