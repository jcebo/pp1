import json
with open("notowania.json", encoding='utf-8') as handle:
    data = json.loads(handle.read())
print('NBP – bieżące notowania walut '+'\n'+'data: '+data[0]["effectiveDate"],'\n'+'waluta'+35*' '+'kurs'+'\n'+50*'=')
for n in range(len(data[0]["rates"])):
    print(data[0]["rates"][n]["currency"]+(40-len(data[0]["rates"][n]["currency"]))*' ',data[0]["rates"][n]["mid"])