from math import * # Pour utiliser pi

def cercle(r):
    """
    :entrée r: float
    :sortie d: float
    :sortie p: float
    :sortie s: float
    :pré-cond: r ≥ 0
    :post-conf: d contient le diamètre d'un cercle de centre r,
                p contient le périèmtre d'un cercle de centre r,
                s contient la surface d'un cercle de centre r
    """

    if(r >= 0):
        d = 2*r                # diamètre
        p = 2*pi*r        # périmètre
        s = pi*r*r      # surface

        return d, p, s

# Test de cercle() avec un rayon r = 4
d, p, s = cercle(4.0)
print("Cercle de rayon 4 : d=" + "{:.3f}".format(d) + ", p=" + "{:.3f}".format(p) + ", s=" + "{:.3f}".format(s))

#####################################

def coef_droite(x1, y1, x2, y2):
    """
    :entrée x1: float
    :entrée y1: float
    :entrée x2: float
    :entrée y2: float
    :sortie a: float
    :sortie b: float
    :pré-cond: les deux points de coordonnées (x1, y1) et (x2, y2)
               sont distincts et ne sont pas alignés verticalements,
               autrement dit x1 ≠ x2
    :post-cond: a et b sont les coefficients de la droite passant par
                les deux points de coordonnées (x1, y1) et (x2, y2),
                autrement dit y1 = a×x1 + b et y2 = a×x2 + b

    """

    if(x1 != x2):

        a = (y2-y1)/(x2 - x1) # Coef a
        b = (y1 - a*x1) # Coef b

        return a, b

# Test de coef_droite()

a, b = coef_droite(2.0,5.0,6.0,8.0)
print("Coefficients :: a=" + "{:.3f}".format(a) + " et b=" + "{:.3f}".format(b))
