from math import * # Pour la fonction racine carrée (sqrt())

def duree_en_secondes(j, h, m, s):
    """
    :entrée j: int
    :entrée h: int
    :entrée m: int
    :entrée s: float
    :sortie ds: float
    :pré-cond: j > 0 , 0 ≤ h < 24 , 0 ≤ m < 60, 0 ≤ s < 60
    :post-cond: ds est le nombre de secondes correspond à
                une durée de j jours, h heures, m minutes et s secondes.
    """

    if((j > 0) and (0 <= h < 24) and (0 <= m < 60) and (0 <= s < 60)):

        ds = j*86400 + h*3600 + m * 60 + s

        return ds

# Test de duree_en_secondes()
ds = duree_en_secondes(10,23,5,6)
print("10 jours, 23h 5min et 6s <=> " + "{:.6f}".format(ds) + "s")

ds = duree_en_secondes(15,20,56,10)
print("15 jours, 20h 56min et 10s <=> " + "{:.6f}".format(ds) + "s")

######################

def secondes_en_duree(sec):
    """
    :entrée sec: int
    :sortie j: int
    :sortie h: int
    :sortie m: int
    :sortie s: int
    :pré-cond: sec ≥ 0
    :post-cond: sec est le nombre de secondes correspond à
                une durée de j jours, h heures, m minutes et s secondes
                avec j > 0 , 0 ≤ h < 24 , 0 ≤ m < 60, 0 ≤ s < 60 .
    """

    if(sec >= 0):

        j = sec / 86400
        if(j < 1): j = 0
        h = (sec % 86400) / 3600
        m = (sec % 3600) / 60
        s = (sec % 3600) % 60

        return int(j), int(h), int(m), int(s)


# Test de secondes_en_duree()
j, h, m, s = secondes_en_duree(56235)
print("56235s <=> " + str(j) + " jours, " + str(h) + "h " + str(m) + "min " + str(s) + "s")

j, h, m, s = secondes_en_duree(4526052)
print("4526052s <=> " + str(j) + " jours, " + str(h) + "h " + str(m) + "min " + str(s) + "s")

j, h, m, s = secondes_en_duree(45216564)
print("45216564s <=> " + str(j) + " jours, " + str(h) + "h " + str(m) + "min " + str(s) + "s")