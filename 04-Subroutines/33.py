def fib(n):
    a,b=0,1
    for i in range(n-1):
        a,b=b,a+b
    return a
x=1
while x<21:
    print (fib(x),end=' ')
    x+=1
    