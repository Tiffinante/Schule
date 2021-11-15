print("Aufgabe 1")
alter = int(input("dein alter:"))
if alter < 19 and alter > 13:
    print("Du bist Jugentlich")
elif alter >= 18:
    print("HGW... Du bist Volljehrig")
else:
    print("Im Anakin Skywalker and i like junglings :)")

print("Aufgabe 2")
element = input("ein element kürzel deiner wahl:")
if element == "Li" or element == "Na" or element == "K" or element == "Rb" or element == "Cs":
    print("Dein Metall ist ein Alkanimetall")
else:
    print("Sorry bro du hast kein cooles Alkanimetall")

print("Aufgabe 3")
jahr = int(input("ein jahr deiner wahl:"))
if jahr % 4 == 0 and jahr % 100 != 0 or jahr % 400 == 0:
    print("jo ist nh schalt jahr")
else:
    print("nope ist keins")