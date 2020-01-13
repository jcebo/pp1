wzrost = int(input('Podaj wzrost: '))
waga = float(input('Podaj wagę: '))
assert type(wzrost)==int, 'Wzrost musi być liczbą całkowitą'
assert wzrost>=150 and wzrost<=220, 'Wzrost musi być z przedziału 150-220'
assert waga>=40 and waga <=150, 'Waga musi być z przedziału 40-150'
wzrost=wzrost/100
print ('Twoje BMI to: ')
print(waga/wzrost**2)