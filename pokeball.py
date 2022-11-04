import random

pokemon = [
    ['Charmander', 'Fire', 56, 23, 13, 2],
    ['Squirtle', 'Water', 30, 40, 8, 1],
    ['Bulbasaur', 'Boil', 25, 23, 9, 3],
    ['Pikachu', 'Electricity', 45, 25, 16, 3]
]

oponent = [
    ['Charmander', 'Fire', 57, 20, 13, 2],
    ['Squirtle', 'Water', 27, 40, 9, 1],
    ['Bulbasaur', 'Boil', 26, 22, 10, 3],
    ['Pikachu', 'Electricity', 45, 25, 16, 2],
    ['Pidgey', 'Flying', 37, 19, 18, 4],
    ['Haunter', 'Poison', 20, 10, 19, 5]
]

def pos():
    a, b = 0, len(oponent) - 1
    return random.randint(a, b)
    
