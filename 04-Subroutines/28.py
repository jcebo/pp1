jezyki=['Java','Python','JS','c++','c#','ruby','perl','php','c','android']
wartosci=[61,47,37,32,26,18,14,14,9,7]
def rysujWykres(jezyki,wartosci):
    for n in range(len(jezyki)):
        print((10-len(jezyki[n]))*' '+jezyki[n] + ':',end=' ')
        print(int(wartosci[n]/4)*'#')
rysujWykres(jezyki,wartosci)