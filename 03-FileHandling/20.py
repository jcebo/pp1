numbers=[]
import re
with open('numbers.txt','r') as file:
    for n in file:
        numbers.append(int(n))
file.close()

with open('evennumbers.txt','w') as file1:
    for n in numbers:
        if n%2==0 and n>=0:
            file1.write(str(n)+'\n')