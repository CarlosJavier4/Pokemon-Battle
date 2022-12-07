def effectiveness(type_atk, type_def, _atk):

    """
        effectiveness(type1, type2) --> The paraments of function are str.
        
        The values supported by the attacker are:'fire', 'water', 'boil', 'electricity' (type_atk)
        The values supported by the defender are:
            'fire', 'water', 'boil', 'electricity', 'earth', 'poison', 'bug', 'rock', 'flying', 'ice' and 'steel'.
        
        The function makes use of a matrix, where types[i][0] is the attacker's type, and types[i][1]
        are the types they are weak against and the rest they are strong against.
        
    """
    
    type_atk, type_def  = type_atk.lower(), type_def.lower()
    
    types = [
        ['fire', ['water', 'rock', 'earth'], ['steel', 'ice', 'boil', 'bug']],
        ['water', ['electricity', 'boil'], ['fire', 'earth', 'rock']],
        ['boil', ['fire', 'ice', 'poison', 'flying', 'bug'], ['water', 'earth', 'rock']],
        ['electricity', ['earth'], ['water', 'flying']] 
    ]
    
    for i in range(0, len(types)):
        if type_atk == types[i][0]:
            if type_def in types[i][2]:
                return 3
            else:
                return _atk / 2 - 10
        else:
            return 1

def battle(typeAtk, typeDef, _atk, _def):
    valueOfAtk = int(5 * (_atk // _def) * atributes.effectiveness(typeAtk, typeDef, _atk) + random.randint(1, 4))
    return valueOfAtk if valueOfAtk < 60 else valueOfAtk - 60

def WhoAttack(pokemon1, v1, pokemon2, v2):
    return (pokemon1 if v1 >= v2 else pokemon2)
    
