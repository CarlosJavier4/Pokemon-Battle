import atributes
import random

def battle(typeAtk, typeDef, _atk, _def):
    valueOfAtk = int(5 * (_atk // _def) * atributes.effectiveness(typeAtk, typeDef, _atk) + random.randint(1, 4))
    return valueOfAtk if valueOfAtk < 60 else valueOfAtk - 60
    

