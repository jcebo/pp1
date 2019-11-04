def wystepuje(liczba,tablica):
    if liczba in tablica:
        print(f"liczba {liczba}"+ "\n" f"tablica: {tablica}")
        print ("Podana liczba występuje w tablicy")
        
wystepuje(23,[15, 38, 7, 23, 14])
