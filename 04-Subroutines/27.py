tekst='Nam strzelać nie kazano. Wstąpiłem na działo. I spojrzałem na pole, dwieście armat grzmiało. Artyleryji ruskiej ciągną się szeregi, Prosto, długo, daleko, jako morza brzegi.'
def ile(a,tekst):
    i=0
    for n in tekst.lower():
        if n==a:
            i+=1
    return i
     
a=input('Podaj samogloske: ')
print(f'Samogloska wystepuje {ile(a,tekst)} razy w tekscie')