def cyfry_tel():
    for n in range(9):
        if n in range(2,9,3):
            print (n+1, " ", end=" "+ "\n")
        else:
            print (n+1, " ", end=" ")
            