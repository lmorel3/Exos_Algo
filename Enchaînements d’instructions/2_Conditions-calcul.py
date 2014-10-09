from math import * # Pour la fonction racine carrée (sqrt())

def plus_petit(a, b, c):
    """
    :entree a: int
    :entree b: int
    :entree c: int
    :sortie pp: int
    :pré-cond: (aucune)
    :post-cond: pp = le plus petit nombre de l'ensemble {a, b, c}
    """

    pp = 0
    if(a < b):
        if(a < c): # a
            pp = a # a < b < c
        else: # c < a
            pp = c # c < a < b
    else: # b < a
        if(b < c):
            pp = b # b < c < a
        else: # c < b
            pp = c # c < b < a

    return pp

# Tests de plus_petit()
pp1 = plus_petit(2,3,5)
pp2 = plus_petit(5,3,20)
pp3 = plus_petit(41,40,5)

print("plus_petit(2,3,5) => " + "{:.3f}".format(pp1))
print("plus_petit(5,3,20) => " + "{:.3f}".format(pp2))
print("plus_petit(41,40,5) => " + "{:.3f}".format(pp3))

###########################

def racines_2nd_degre(a, b, c):
    """
    :entrée a: float
    :entrée b: float
    :entrée c: float
    :sortie r1: float ou None
    :sortie r2: float ou None
    :pré-cond: a ≠ 0
    :post-cond: si l'équation ax²+bx + c n'a pas de racine réelle,
                r1 = r2 = None,
                sinon, si elle a exactement une racine réelle,
                r1 a pour valeur cette racine et r2 = None,
                sinon (l'équation a deux racine réelles),
                r1 et r2 ont pour valeur ces deux racines
    """

    if(a != 0):

        delta = b*b - 4*a*c

        r1 = 0.0
        r2 = 0.0

        # J'ai mis -999.999 au lieu de None pour que
        # ça puisse s'afficher dans le print sans erreurs..

        if(delta == 0):
            r1 = (-b)/(2*a)
            r2 = -999.999 # Une seule racine
        elif(delta > 0):
            r1 = (-b-sqrt(delta))/(2*a)
            r2 = (-b+sqrt(delta))/(2*a)
        else: # delta < 0
            r1 = -999.999 # None
            r2 = -999.999 # None

        return r1, r2

# Test de racines_2nd_degre()
r1, r2 = racines_2nd_degre(5.0,2.0,3.0)
print("5x² + 2x + 3 :: r1=" + "{:.3f}".format(r1) + " et r2=" + "{:.3f}".format(r2))

r3, r4 = racines_2nd_degre(-5.0,10.0,5.0)
print("-5x² + 10x + 5 :: r1=" + "{:.3f}".format(r3) + " et r2=" + "{:.3f}".format(r4))