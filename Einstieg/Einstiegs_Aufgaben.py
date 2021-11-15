print('''   
            #############################
            ----->Einstiegsaufgaben<-----
            #############################''')

# Aufgabe 0
print(" ")
print("Aufgabe 0")
print("Hello World")
print("Hello World")

# Aufgabe 1
print(" ")
print("Aufgabe 1")
print("Grundrechenarten")
a = int(input("wähle eine ganze zahl a:"))
b = int(input("wähle eine ganze zahl b:"))
print(a + b)
print(a - b)
print(a * b)
print(a / b)

# Aufgabe 2
print(" ")
print("Aufgabe 2")
print("Dreieck")
print("")
print("NUR GANZ ZAHLEN")
h = int(input("wähle die höhe des dreiecks:"))
g = int(input("wähle eine grund seite:"))
print((h * g) / 2)

# Aufgabe 3
print(" ")
print("Aufgabe 3")
print("Tausch")
print("")
a = 5
b = 3
print("a = 5")
print("b = 3")
input("drücke enter um zu tauschen")
c = a
a = b
b = c
print("a = " + str(a))
print("b = ", b)

# Aufgabe 4
print(" ")
print("Aufgabe 4")
print("Niederschlag")
print("")
april = 12
mai = 14
juni = 8

print("1 schritt")
print((april + mai + juni) / 3)

print("2 schritt")
print(april + mai + juni)
amj = april + mai + juni
print(amj / 3)

answer = str(input("Willst du das programm beenden? y or n:"))
if answer == "y" or answer == "Y":
    quit()
else:
    print("Sorry du aber das programm geht nicht weiter :(")
    input("press enter")
    quit()
