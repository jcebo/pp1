x=1
y=2
sp=0 #suma parzystych
sn=0 #suma nieparzystych
while x<51:
    sn+=x
    x+=2

while y<51:
    sp+=y
    y+=2
    
print("Suma liczb parzystych i nieparzystych to:",sp,"i",sn)