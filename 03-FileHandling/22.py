import re
with open('students.txt','r') as file:
    for n in file:
        y=re.split(',',n)
        if y[2]!='age':
            if int(y[2])<30:
                print('{}  {}  {}'.format(y[0],y[1],y[4]))