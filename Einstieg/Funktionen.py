
def dubble(n):
    n *= 2

def dreieck_zur_hypotenose(a, b):
    (a * b) / 2

def wellcome():
    print('''
            #######################################################
            ##                                                   ##
            ##      Ein Legänderes Programm von Mika Kattau      ##
            ##          --Programm Name--                        ##
            ##                                                   ##
            #######################################################
    ''')

# WICHTIG!
def binaer(dezimalzahl):
    list1 = []
    while dezimalzahl > 0:
        zwischen_Summe = dezimalzahl % 2
        list1.insert(0, zwischen_Summe)
        dezimalzahl //= 2
    s = ""
    for nr in list1:
        s += str(nr)
    i = int(s)
    return i

# WICHTIG
def dezimal(binaerzahl):
    ergebnis = 0
    multiplikator = 1
    binaerzahl = str(binaerzahl)

    while len(binaerzahl) > 0:
        len_binaer = len(binaerzahl) - 1
        stelle = binaerzahl[len_binaer]

        if stelle == "1":
            ergebnis += multiplikator
            multiplikator *= 2
            binaerzahl = binaerzahl[:-1]

        elif stelle == "0":
            multiplikator *= 2
            binaerzahl = binaerzahl[:-1]

    return ergebnis

dezimal()