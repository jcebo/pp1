import re
liczby=[]
with open('numbers.txt','r') as file: 
    for n in file: 
        liczby.append(int(n))
liczby.sort()
for n in liczby:
    print(f'{n}',end=' ')