import random
wylosowana=random.sample(range(1,7), 1) #komputer losuje 1 liczbe z zakresu 1-6
zgad=int(input("Podaj, ile oczek kostki wyrzucił komputer: "))#gracz wprowadza liczbę
print(f"Komputer wyrzucił: {wylosowana[0]}")
if (wylosowana[0]==zgad):
    print("Brawo, zgadłeś/aś!")
else:
    print("Niestety, to nie ta liczba")