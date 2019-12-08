class Kontakt:
    def __init__(self,nazwa,email,telefon):
        self.nazwa = nazwa
        self.email = email
        self.telefon = telefon
class ListaKontaktow:
    def __init__(self,):
        self.kontakt = []
    def dodaj(self,kontakt):
        self.kontakt.append(kontakt)
    def wyswietl(self):
        for x in self.kontakt:
            print(f'{x.nazwa}'+' '*(16-len(x.nazwa))+f'{x.email}'+' '*(16-len(x.email))+f'{x.telefon}')

k1 = Kontakt('Kowalski Jan', 'jank@onet.pl', '555234000')
k2 = Kontakt('Borek Patrycja','bp@o2.pl','232000199')
k3 = Kontakt('Maj Piotr','maj@google.pl','222999100')
k4 = Kontakt('Adamczyk Anna','ada@poczta.pl','100200300')

myList = ListaKontaktow()

myList.dodaj(k1)
myList.dodaj(k2)
myList.dodaj(k3)
myList.dodaj(k4)

myList.wyswietl()
