import re
counter=0
sum=0
with open('numbersinrows.txt','r') as file:
    for n in file:
        tab=re.split(',',n)
        counter+=len(tab)
        for i in tab:
            sum+=int(i)
print('Ilość liczb: {}\nSuma: {}'.format(counter,sum))