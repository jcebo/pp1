import statistics
salary=[21600, 4350, 3920, 5590, 3250, 4010]
a=statistics.mean(salary)
salary.sort()
b=statistics.median(salary)
c=statistics.stdev(salary)
print(f'Średnia arytmetyczna pensja to {a}, mediana {b}, a odchylenie standardowe {c}')