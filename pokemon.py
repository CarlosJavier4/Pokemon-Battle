from time import sleep
import atributes
import containerPokemon

print('-----------------Start the battle-------------------')

# Choose the enemy pokemon
idx = containerPokemon.pos() 
name_pokemon_oponent = containerPokemon.oponent[idx].imp()[0] 
type_pokemon_oponent = containerPokemon.oponent[idx].imp()[1] 
atk_pokemon_oponent = containerPokemon.oponent[idx].imp()[2] 
def_pokemon_oponent = containerPokemon.oponent[idx].imp()[3] 
vel_pokemon_oponent = containerPokemon.oponent[idx].imp()[4] 

print(f'\t ==> Your oponent has sent {name_pokemon_oponent}')
print(f'\t Type: {type_pokemon_oponent}')
print(f'\t Atk: {atk_pokemon_oponent}   Def: {def_pokemon_oponent}')
sleep(1)
print('\nQuickly, choose your pokemon to defend yourself.\n')
sleep(2)

cont = 1

# Choose your pokemon
cantPokemon = len(containerPokemon.pokeball)

for i in range(0, cantPokemon):
    aux = containerPokemon.pokeball[i].imp()
    print(f'\t ==> {cont}.{aux[0]} \n\t type: {aux[1]}  //  Atk: {aux[2]}  //   Def: {aux[3]} \n')
    cont = cont + 1
    sleep(1.6)
    
position = int(input('-> Select the number: '))
position = atributes.checkPosition(position, cont)

name_pokemon = containerPokemon.pokeball[position - 1].imp()[0]
type_pokemon = containerPokemon.pokeball[position - 1].imp()[1]
atk_pokemon = containerPokemon.pokeball[position - 1].imp()[2]
def_pokemon = containerPokemon.pokeball[position - 1].imp()[3]
vel_pokemon = containerPokemon.pokeball[position - 1].imp()[4]

print(f'Great!! {name_pokemon} is an excellent option')
sleep(0.50)
print('\n')

# Who attack...
gamer = atributes.WhoAttack(name_pokemon, vel_pokemon, name_pokemon_oponent, vel_pokemon_oponent)

life_pokemon, life_oponent = 60, 60  #Using a tuple

while life_pokemon > 0 and life_oponent > 0:

    print(f'{gamer} prepares to attack...', end = ' ')
    sleep(0.50)

    ptos = atributes.battle(type_pokemon, type_pokemon_oponent, atk_pokemon, def_pokemon_oponent)
    print(f'{gamer} dealt {ptos} damage...', end=' ')
    
    sleep(1)
    
    if gamer == name_pokemon:
        swap_name = name_pokemon_oponent
        life_oponent = life_oponent - ptos
        if life_oponent > 0: 
            print(f'{swap_name} hit points are: {life_oponent}\n')
    elif gamer == name_pokemon_oponent:
        swap_name = name_pokemon
        life_pokemon = life_pokemon - ptos
        if life_pokemon > 0: 
            print(f'{swap_name} hit points are: {life_pokemon}\n')

    # Swap the names
    gamer, swap_name = swap_name, gamer
    # Swap the types
    type_pokemon, type_pokemon_oponent = type_pokemon_oponent, type_pokemon
    

if life_pokemon <= 0:
    print(f'\n==> {name_pokemon} has lost\n\n')
else:
    print(f'\n==> {name_pokemon_oponent} has lost\n\n')
