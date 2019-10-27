x=int(input("Podaj Liczbę: "))


c=0
c2=0

t=2
    
    
while c2<x:    
    
    for i in range(1,t):
        if t%i==0:
            c+=1

    if c==1:
        print (t)
        c2+=1
    t+=1
    c=0
