import atributes

def battle(typeAtk, typeDef, _atk, _def):
    """ formula to calculate hit points """
    valueOfAtk = 5 * (_atk / _def) * atributes.effectiveness(typeAtk, typeDef)
    return int(valueOfAtk)
    
