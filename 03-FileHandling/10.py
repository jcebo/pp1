suma=0
with open('numbers.txt','r') as file:
    for n in file:
        suma+=int(n)
print(suma)