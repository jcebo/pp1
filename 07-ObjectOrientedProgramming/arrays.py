from random import randint
class arrays():
    @staticmethod
    def print_in_col(array):
        for c in array:
            print(c)
    def print2(array):
        for n in array:
            if n==array[-1]:
                print (n)
            else:
                print(f'{n},',end='')
    def a(liczba_elementow_tablicy,wartosc_elementow_tablicy):
        tab=[]
        x=0
        while x<liczba_elementow_tablicy:
            tab.append(wartosc_elementow_tablicy)
            x+=1
        print (tab)
    def b(liczba_elementow_tablicy,wartosc_od,wartosc_do):
        tab2=[]
        l=liczba_elementow_tablicy
        m=wartosc_od
        n=wartosc_do
        x=0
        while x<l:
            tab2.append(randint(m,n))
            x+=1
        print(tab2)
    def c(tablica,wartość_od,wartość_do):
        licznik=0
        for n in len(tablica):
            if tablica[n]>=wartość_od and tablica[n]<=wartość_do:
                licznik+=1
        print(licznik)
my_array = [4,1,8,7,2]
arrays.print_in_col(my_array)
