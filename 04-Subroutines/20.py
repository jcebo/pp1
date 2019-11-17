def potega(x,n):
    if n>0:
        return x*potega(x,n-1)
    else:
        return 1
print(f'5 do potegi 3 to {potega(5,3)}')