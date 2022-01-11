import math

# Begrüßung

print("Whats your name")
name = input("Name:")
print(name)
print("Hallo ", name, "!", sep="")
# Manschaft
m1 = input("Manschaft 1:")
m2 = input("Manschaft 2:")
print(m1, "gegen", m2)

# Verdoppler

while True:
    number_x_2 = input("Number*2:")
    if number_x_2.isdecimal():
        print(int(number_x_2) * 2)
        break
    else:
        print("Bitte nur Zahlen!!!")

# Manschaft 2

while True:
    punkte_m1 = input("Die Punkte für M1")
    punkte_m2 = input("Die Punkte für M2")
    if punkte_m1.isdecimal() and punkte_m2.isdecimal():
        break

print(m1, punkte_m1, ":", punkte_m2, m2)
p_m1 = int(punkte_m1)
p_m2 = int(punkte_m2)
if p_m1 > p_m2:
    print("Sieger ist", m1)
elif p_m1 == p_m2:
    print("Unendschieden")
else:
    print("Sieger ist", m2)

# Rechtecksberechnung

while True:
    seite_a = input("Die Seite für a")
    seite_b = input("Die Seite für b")
    if seite_b.isdigit() and seite_a.isdigit():
        einheit = input("ihre einheit:")
        if not(einheit.isdecimal()):
            a = int(seite_a)
            b = int(seite_b)
            break
    elif seite_a.find(",") == 1 or seite_b.find(",") == 1:
        einheit = input("ihre einheit:")
        if seite_a.find(",") == 1:
            seite_a = seite_a.replace(",", ".")
        else:
            print("Falsche eingabe!1")
        if seite_b.find(",") == 1:
            seite_b = seite_b.replace(",", ".")
        else:
            print("Falsche eingabe!2")

        a = float(seite_a)
        b = float(seite_b)
        break
    else:
        print("Falsche eingabe!3")

print("Der Umfang beträgt ", a * 2 + b * 2, einheit, sep="")
print("Die Fläche beträgt ", b * a, einheit, "²", sep="")
print("Die Diagonale beträgt ", math.sqrt((a ** 2) * (b ** 2)), einheit, sep="")
