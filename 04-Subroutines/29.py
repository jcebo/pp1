tab=[2,3,5,2,9,8,1,3,9,1,1,4,7,7,1,4]
tab.sort()
def mediana(tab):
    if len(tab)%2==0:
        a=len(tab)//2
        return (tab[a]+tab[a-1])/2
    else:
        a=len(tab)//2
        return tab[a]
def dom(tab):
    y=0
    for i in range(len(tab)):        
        if tab.count(tab[i])>(tab.count(tab[i-1]))and tab.count(tab[i])>y:
            x=tab[i]
            y=tab.count(tab[i])
    return x
        
        


    