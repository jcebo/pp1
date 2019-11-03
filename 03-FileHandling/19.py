import re
sort=[]
universities=[]
with open('universities.txt','r') as file:
    for n in file:
        universities.append(n)
file.close()

universities.sort()
with open('universities.txt','w') as file:    
    for n in universities:
        file.write(n)
file.close()
