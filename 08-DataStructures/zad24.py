import json

with open("DontMakeMeWait.txt", "r") as f:
    data = f.read()
data=data.replace("\n", "")
data=data.replace("'", "")
data=data.replace(" ", "")
data=data.replace(",", "")
data=data.replace("(", "")
data=data.replace(")", "")
data=data.replace("!", "")
data=data.casefold()
frequencies = {} 
for char in data: 
   if char in frequencies: 
      frequencies[char] += 1
   else: 
      frequencies[char] = 1
with open('zad24.json', 'w') as file:
        json.dump(frequencies, file,indent=2)



