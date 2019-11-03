nrdnia=int(input('Nr dnia Tygodnia: '))
print ('| PN | WT | SR | CZ | PT | SB | ND |')
if nrdnia>0:
    for x in range(nrdnia):
        print('|   ', end =" ")
    
for x in range(1,10):
    if (nrdnia+x-1)==7 or (nrdnia+x-1)==14:
        print('|')
    print('| ',x, end =" ")
    
for x in range(10,31):
    if (nrdnia+x-1)%7==0:
        print('|')
    print('|',x, end =" ")    
    
for x in range (5-nrdnia):
        print('|   ', end =" ")
if nrdnia!=6:
    print('|')
else:
    for x in range (6):
        print('|   ', end =" ")
    
    print('|')
        