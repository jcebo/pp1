#tablica=[4,3,7,1,3]
def suma(tablica):
    print("Tablica:  ",end=" ")
    for i in range(len(tablica)):
        print(tablica[i],end=" ")
    print(f"\n Suma tablicy to: {sum(tablica)}")