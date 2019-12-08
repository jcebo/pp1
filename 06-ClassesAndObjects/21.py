class Statistic:
    def __init__(self):
        self.tab = []
    def split(self):
        for x in range(0,self.tab-1):
            print(x,end=', ')
        print(self.tab[-1])
    def najwieksza(self):
        return max(self.tab)
    def najmniejsza(self):
        return min(self.tab)
    def srednia(self):
        return sum(self.tab)/len(self.tab)
    def mediana(self):
        import statistics
        return statistics.median(self.tab)
    def dodaj(self):
        self.tab.append(int(input('Podaj liczbę: ')))
    def show(self):
        print(f'Najmniejsza liczba: {self.najmniejsza()}\nNajwiększa liczba: {self.najwieksza()}\nŚrednia arytmetyczna: {self.srednia()}\nMediana: {self.mediana()}')
liczby = Statistic()
for x in range(5):
    liczby.dodaj()
liczby.show()