from random import randint

class Pokemon():
    def __init__(self, name, types, atk, defe, vel):
        self.name = name
        self.types = types
        self.atk = atk
        self.defe = defe
        self.vel = vel
    def imp(self):
        return [self.name, self.types, self.atk, self.defe, self.vel]

pokeball, oponent = [], []

# Add your pokemons to the pokeball

pokemon = Pokemon('Charmander', 'Fire', 56, 23, 13)
pokeball.append(pokemon)

pokemon = Pokemon('Squirtle', 'Water', 42, 40, 8)
pokeball.append(pokemon)

pokemon = Pokemon('Bulbasaur', 'Boil', 30, 23, 9)
pokeball.append(pokemon)

pokemon = Pokemon('Pikachu', 'Electricity', 45, 25, 16)
pokeball.append(pokemon)

# Add the oponent's pokemon

pokemon = Pokemon('Charmander', 'Fire', 57, 20, 13)
oponent.append(pokemon)

pokemon = Pokemon('Squirtle', 'Water', 30, 40, 9)
oponent.append(pokemon)

pokemon = Pokemon('Bulbasaur', 'Boil', 29, 22, 10)
oponent.append(pokemon)

pokemon = Pokemon('Pikachu', 'Electricity', 45, 25, 16)
oponent.append(pokemon)

pokemon = Pokemon('Pidgey', 'Flying', 37, 19, 18)
oponent.append(pokemon)

pokemon = Pokemon('Haunter', 'Poison', 20, 10, 19)
oponent.append(pokemon)

def pos(): return randint(0, len(oponent)-1) #Select a position random
