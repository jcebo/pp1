import re
sum=0
komunikat = 'wtorek - 23C, środa - 17C, czwartek 25C'
cyfry = re.findall('\d{2}',komunikat)
for n in range(len(cyfry)):
    sum+=int(cyfry[n])
print(f'Srednia temp. to: {sum/len(cyfry)} C')