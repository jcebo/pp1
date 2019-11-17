def sumcyfr(n):
    if n>=10:
        return sumcyfr(n//10)+sumcyfr(n-sumcyfr(n//10)*10)
    else:
        return n