import random
liczby = random.sample(range(1, 7), 3) #stworzenie tablicy składającej się z 3 liczb w zakresie 1-6 
print(f"Wylosowane liczby to: {liczby}")#pokaz wylosowane liczby
suma=liczby[0]+liczby[1]+liczby[2]#sumowanie wylosowanych liczb
print(f"Suma tych liczb to: {suma}")#pokaz zsumowane liczby

