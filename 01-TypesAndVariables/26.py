wzrost=float(input("Podaj swój wzrost w cm: ")) #Wczytanie wzrostu
waga=float(input("Podaj swoją wagę w kg: ")) #Wczytanie wagi
wzrost=wzrost/100
bmi=waga/(wzrost*wzrost)
if (bmi<18.5):
    print(f"Twoje BMI to: {bmi} - masz niedowagę!")
elif (bmi>=18.5 and bmi<25):
    print(f"Twoje BMI to: {bmi} - wszystko w porządku!")
else: 
    print(f"Twoje BMI to: {bmi} - masz nadwagę!")