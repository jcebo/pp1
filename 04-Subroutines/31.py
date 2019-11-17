tab=[2, 5, 4, 1, 8, 7, 4, 0, 9]
new=[]
def reverse(tab):
    x=len(tab)-1
    for n in range(len(tab)):
        new.append(tab[x])
        x-=1
       