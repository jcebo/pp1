x=float(input("wprowadz punkt x: "))
y=float(input("wprowadz punkt y: "))
if (x>0 and y>0):
    print(f"Punkt ({x},{y}) znajduje sie w 1 cwiartce ukladu wspolrzednych")
elif (x>0 and y<0):
    print(f"Punkt ({x},{y}) znajduje sie w 4 cwiartce ukladu wspolrzednych")
elif (x<0 and y<0):
    print(f"Punkt ({x},{y}) znajduje sie w 3 cwiartce ukladu wspolrzednych")
elif (x<0 and y>0):
    print(f"Punkt ({x},{y}) znajduje sie w 2 cwiartce ukladu wspolrzednych")

    

