import math

try:
    number = float(input('Enter any number: '))
    print (f'sqrt({number}) = {math.sqrt(number)}' )
except ValueError:
    print('Podaj liczbę')
#except number
except:
    print('Please enter a valid number greater than 0')