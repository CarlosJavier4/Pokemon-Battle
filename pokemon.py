import atributes
import calcAtk
import pokeball
import check
import time

print('-----------------Start the battle-------------------')

# Choose the enemy pokemon
idx = pokeball.pos() 
name_pokemon_oponent = pokeball.oponent[idx][0] 
type_pokemon_oponent = pokeball.oponent[idx][1]  
atk_pokemon_oponent = pokeball.oponent[idx][2]
def_pokemon_oponent = pokeball.oponent[idx][3]
vel_pokemon_oponent = pokeball.oponent[idx][4]

print(f'\t ==> Your oponent has sent {name_pokemon_oponent}')
print(f'\t Type: {type_pokemon_oponent}')
print(f'\t Atk: {atk_pokemon_oponent}   Def: {def_pokemon_oponent}')

time.sleep(1)

print('\nQuickly, choose your pokemon to defend yourself.\n')
time.sleep(2)

cont = 1

# Choose your pokemon
for i in pokeball.pokemon:
    print(f'\t ==> {cont}.{i[0]} \n\t type: {i[1]}  //  Atk: {i[2]}  //   Def: {i[3]} \n')
    cont = cont + 1
    time.sleep(1.6)
    
position = int(input('-> Select the number: '))
position = check.checkPosition(position, cont)

name_pokemon = pokeball.pokemon[position - 1][0]
type_pokemon = pokeball.pokemon[position - 1][1]
atk_pokemon = pokeball.pokemon[position - 1][2]
def_pokemon = pokeball.pokemon[position - 1][3]
vel_pokemon = pokeball.pokemon[position - 1][4]

print(f'Great!! {name_pokemon} is an excellent option')
time.sleep(0.50)
print('\n')

# Who attack...
gamer = atributes.WhoAttack(name_pokemon, vel_pokemon, name_pokemon_oponent, vel_pokemon_oponent)

life_pokemon, life_oponent = 60, 60

while life_pokemon > 0 and life_oponent > 0:

    print(f'{gamer} prepares to attack...', end = ' ')
    time.sleep(0.50)

    ptos = calcAtk.battle(type_pokemon, type_pokemon_oponent, atk_pokemon, def_pokemon_oponent)
    print(f'{gamer} dealt {ptos} damage...', end=' ')
    
    time.sleep(1)
    
    a, b = 0, 0
    
    if gamer == name_pokemon:
        a = name_pokemon_oponent
        life_oponent = life_oponent - ptos
        if life_oponent > 0: 
            print(f'{a} hit points are: {life_oponent}\n')
    elif gamer == name_pokemon_oponent:
        a = name_pokemon
        life_pokemon = life_pokemon - ptos
        if life_pokemon > 0: 
            print(f'{a} hit points are: {life_pokemon}\n')

    # Swap the names
    b = gamer
    gamer = a
    a = b

    # Swap the types
    aux = type_pokemon
    type_pokemon = type_pokemon_oponent
    type_pokemon_oponent = aux
    

if life_pokemon <= 0:
    print(f'\n==> {name_pokemon} has lost\n\n')
else:
    print(f'\n==> {name_pokemon_oponent} has lost\n\n')





