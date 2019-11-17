def podatek(dochod):
    if dochod<=5000:
        return (0.17*dochod)
    else:
        return 0.17*5000+0.32*(dochod-5000)
    
dochod=float(input('Podaj dochód: '))
print(f'Nalezny podatek to: {round(podatek(dochod),2)}')