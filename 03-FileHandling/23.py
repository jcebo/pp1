import re
sum=0
with open('land.txt','r') as file:
    n=file.read()
digits=re.findall('\d',n)
for i in digits:
    sum+=int(i)
print('Suma: {}'.format(sum))
