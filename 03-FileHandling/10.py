with open('numbers.txt','r') as file:
    for line in file:
        print(line, end=' ')
        sum = sum(line[0:10])
        