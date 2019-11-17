def wyraz(n):
    if n>2:
        return wyraz(n-2)+wyraz(n-1)
    elif n==2:
        return wyraz(1)+1
    elif n==1:
        return 0
x=1
while x<21:
    print(wyraz(x),end=' ')
    x+=1