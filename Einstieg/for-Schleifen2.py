import math

print('''1. Aufgabe: Pi''')
i = 0
n = 1
for k in range(n+1):
    i += (-1)**k / (2 * k + 1)
print(i)
print(math.pi/4)

print('''2. Aufgabe: Schachbrett''')
reis = 1
for i in range(1, 65):
    reis *= 2
print(f"{reis} Reiskörner")

print('''3. Bevölkerungswachstum''')
i = int(input("wieviele Jahre wollen sie sehen:"))
print("{:<8}{:<21}{:<11}{:<17}".format("Jahr", "Anfangspopulation", "Zuwachs", "Endpopulation"))
anfangspopulation = 6.125 # 2000
star = ((20/100) * anfangspopulation) + anfangspopulation
year = 0
while True:
    for nix in range(1, i + 1):
        zuwachs = (anfangspopulation / 100) * 1.5
        zuwachs_round = round(zuwachs, 3)
        endpopulation = round(anfangspopulation + zuwachs, 3)
        year += 1
        if endpopulation > star:
            year_str = str(year) + "*"
        else:
            year_str = year
        print("{:<8}{:<21}{:<11}{:<17}".format(year_str, anfangspopulation, zuwachs_round, endpopulation))
        anfangspopulation = endpopulation
    print("...")
    while True:
        answer = input("witer? J oder N:")
        if answer.lower() == "n":
            break
        elif answer.lower() == "j":
            i = 5
            break
        else:
            print("Bitte nur J oder N!")
    if answer.lower() == "n":
        break


print('''4. Dominosteine''')
for x in range(7):
    for stein in range(7):
        print("({:1}/{:1})".format(stein, x), end=" ")
    print("")
