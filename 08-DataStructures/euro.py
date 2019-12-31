import json
with open("euro.json") as handle:
    data = json.loads(handle.read())
print('NBP – 10 ostatnich notowań EURO'+'\n'+'Data',8*' ','Kupno',2*' ','Sprzedaż'+'\n'+30*'=')
for n in range(len(data["rates"])):
    print(data["rates"][n]["effectiveDate"],2*' ',data["rates"][n]["bid"],(7-len(str(data["rates"][n]["bid"])))*' ',data["rates"][n]["ask"])