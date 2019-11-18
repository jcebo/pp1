import csv
with open('employees.csv', newline='') as f:
    linia=0
    reader = csv.reader(f)    
    for row in reader:
        print(f' if {linia}=0:
        ',end=' ')
        print(f'{row[0]} {row[1]} {row[2]} {row[3]}')
        linia+=1

if linia==0:
    print('#')