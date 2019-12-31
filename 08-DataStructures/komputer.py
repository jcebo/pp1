import json
komputer={"marka_CPU":"Intel",
          "szybkość_CPU": 3.4,
          "podzespoły":["procesor","płyta główna","karta graficzna"],
          "działający": True,
          "rok zakupu": 2015
}
with open('komputer.json', 'w', encoding='utf-8') as f:
    json.dump(komputer, f, ensure_ascii=False, indent=2)