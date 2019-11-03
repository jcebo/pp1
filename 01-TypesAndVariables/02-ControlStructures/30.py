pin = input("Podaj pin: ")

for i in range(2):
    if (pin=="0805"):
        print("Pin prawidłowy")
        exit()
    else:
        print("Pin nieprawidłowy")
        pin = int(input("Podaj pin: "))
print("Pin nieprawidlowy. Karta zablokowana")   