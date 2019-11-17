import random
def rzucKostka():
    x=random.randint(1,6)
    y=random.randint(1,6)
    z=random.randint(1,6)
    print(f'Wyrzucone oczka to: {x},{y},{z} \nIch suma to {x+y+z}')