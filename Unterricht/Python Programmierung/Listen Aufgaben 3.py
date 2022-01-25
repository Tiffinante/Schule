import random
'''# Aufgabe 1
mylist = [1, 1, 23, 6, 848, 37, 57, 4, 6, 334, 34, 34, 45, 44, 123, 879, 545, 9]
mylisttotal = []
c = 0
while True:
    print(mylist)
    listbis = input("Wie viele zahlen sollen eingelesen werden? max " + str(len(mylist)) + " :")
    if listbis.isdecimal():
        listbis = int(listbis)
        if 0 < listbis < len(mylist) + 1:
            for i in mylist:
                mylisttotal.append(i)
                c += 1
                if c == listbis:
                    break
            break
        else:
            print("Bitte nur von 1 bis " + str(len(mylist)))
    else:
        print("Bitte Zahlen")
print(mylisttotal)
mylistgerade = []
mylistungrade = []
for i in mylisttotal:
    if i % 2 == 0:
        mylistgerade.append(i)
    else:
        mylistungrade.append(i)

summeG = 0
summeU = 0
for i in mylistgerade:
    summeG += i
for i in mylistungrade:
    summeU += i

print(f"""
Gerade Zahlen:
Anzahl = {len(mylistgerade)}
Summe = {summeG}

Ungerade Zahlen:
Anzahl = {len(mylistungrade)}
Summe = {summeU}
""")'''

# Aufgabe 2
eingabe = [1, 5, 4, 5, 7, 6, 8, 6, 5, 4, 5, 4]
geglaettet = []
for i in range(len(eingabe)):
    if i == (len(eingabe) - 1):
        n = i
    else:
        n = i + 1
    if i == 0:
        geglaettet.append((eingabe[i] + eingabe[n]) // 2)
    else:
        geglaettet.append((eingabe[i] + eingabe[i - 1] + eingabe[n]) // 3)
print(geglaettet)

# Aufgabe 3
mylist = []
for i in range(1, 10):
    mylist.append(random.randrange(1, 1000))
print(mylist)
mylist.sort()
print(mylist)

for i in range(1, 10):
    mylist.append(random.randrange(1, 1000))
print(mylist)
while True: