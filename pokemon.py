import atributes
import calcAtk
import pokeball
#import check
import time

print('-----------------Start the battle-------------------')

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

for i in pokeball.pokemon:
    print(f'\t ==> {cont}.{i[0]} \n\t type: {i[1]}  //  Atk: {i[2]}  //   Def: {i[3]} \n')
    cont = cont + 1
    time.sleep(1.6)
    
position = int(input('-> Select the number: '))
# Chequear los datos, crear modulo.

name_pokemon = pokeball.pokemon[position - 1][0]
type_pokemon = pokeball.pokemon[position - 1][1]
atk_pokemon = pokeball.pokemon[position - 1][2]
def_pokemon = pokeball.pokemon[position - 1][3]
vel_pokemon = pokeball.pokemon[position - 1][4]

print(f'Great!! {name_pokemon} is an excellent option')
time.sleep(0.50)
print('\n')

gamer = atributes.WhoAttack(name_pokemon, vel_pokemon, name_pokemon_oponent, vel_pokemon_oponent)

print(f'{gamer} prepares to attack...', end = ' ')
time.sleep(0.50)

ptos = calcAtk.battle(type_pokemon, type_pokemon_oponent, atk_pokemon, def_pokemon_oponent)

print(f'{gamer} dealt {ptos} damage..')




