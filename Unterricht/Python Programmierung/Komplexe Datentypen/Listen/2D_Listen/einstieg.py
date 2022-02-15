import random as r

innere_liste_1 = [1, 2, 3]
innere_liste_2 = [4, 5, 6]
innere_liste_3 = [7, 8, 9]

aeussere_liste = [innere_liste_1, innere_liste_2, innere_liste_3]

print(aeussere_liste)

innere_liste_4 = []
aeussere_liste_2 = []

hexa = ("0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F")
n = ""

for y in range(1080):
    innere_liste_4.clear()
    for x in range(1920):
        for i in range(6):
            n += hexa[r.randrange(len(hexa))]
        innere_liste_4.append('#' + n)
        n = ""
    aeussere_liste_2.append(innere_liste_4)

print(aeussere_liste_2)

