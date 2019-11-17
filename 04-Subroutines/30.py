import random
def losowa():
    sumapa=0
    sumanie=0
    for i in range(1000):
        x=random.randrange(1,51)
        if x%2==0:
            sumapa+=x
        else:
            sumanie+=x
    return 'Liczby parzyste: ', round((sumapa/(sumapa+sumanie))*100,2) ,"%", 'Liczby nieparzyste:', round((sumanie/(sumapa+sumanie))*100,2), '%'