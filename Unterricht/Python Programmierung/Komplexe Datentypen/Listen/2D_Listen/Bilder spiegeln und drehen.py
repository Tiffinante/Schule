zeile1 = ["-", "o", "o", "o", "o", "-", "-", "-"]
zeile2 = ["-", "o", "-", "-", "-", "o", "-", "-"]
zeile3 = ["-", "o", "-", "-", "-", "o", "-", "-"]
zeile4 = ["-", "o", "o", "o", "o", "-", "-", "-"]
zeile5 = ["-", "o", "o", "-", "-", "-", "-", "-"]
zeile6 = ["-", "o", "-", "o", "-", "-", "-", "-"]
zeile7 = ["-", "o", "-", "-", "o", "-", "-", "-"]
zeile8 = ["-", "o", "-", "-", "-", "o", "-", "-"]

bild = [zeile1, zeile2, zeile3, zeile4, zeile5, zeile6, zeile7, zeile8]
bild_len = len(bild)

print("bild")
for e in bild:
    for i in range(len(bild)):
        print(e[i], end="")
    print("")
print("")

print("vertikal gespiegelt")
for e in reversed(bild):
    for i in range(len(bild)):
        print(e[i], end="")
    print("")
print("")

print("horizontal gespiegelt")
for e in bild:
    for i in reversed(range(len(bild))):
        print(e[i], end="")
    print("")
print("")

print("90°")
for i in range(bild_len):
    for j in reversed(range(bild_len)):
        print(bild[j][i], end="")
    print("")
print("")

print("180°")
for i in reversed(range(bild_len)):
    for j in reversed(range(bild_len)):
        print(bild[i][j], end="")
    print("")
print("")

print("270°")
for i in reversed(range(bild_len)):
    for j in range(bild_len):
        print(bild[j][i], end="")
    print("")
