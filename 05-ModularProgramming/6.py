import csv
with open('employees.csv', newline='') as f:
    linia=1
    print('#',end='  ')
    reader = csv.reader(f)
    for row in reader:  
           print(f"{2*' '}{row[0]}{(15-len(row[0]))*' '} {row[1]}{(15-len(row[1]))*' '} {row[2]}{(15-len(row[2]))*' '} {row[3]}")
         
           if linia==1:
               print(80*'=')
           if linia<10:
               print(linia, end='  ' )
           if linia==10:
               print(linia, end=' ')
               
           linia+=1
           
    
               
           
               