# Aufgabe 1
mylist = []
while True:
    user = input("Was soll in die liste? :")
    if user == "":
        break
    mylist.append(user)
    print(mylist)

# Aufgabe 2
while True:
    print('''
Hallo, was möchtest du tun?
a) Liste anzeigen
b) Listenelemente hinten anfügen
c) Listenelement an einer bestimmten Stelle einfügen
d) Listenelement löschen
e) Suchen (Vorhandensein bestätigen und Index eines Elementes ausgeben)
    ''')
    selection = input(":")
    if selection:
        if selection == "a":
            print(mylist)
        elif selection == "b":
            mylist.append(input("Was möchten sie hinzufügen:"))
            print(mylist)
        elif selection == "c":
            append = input("Was möchten sie hinzufügen:")
            print("Wo möchten sie es einsetzen?")
            while True:
                pos = input("stelle 1 bis " + str(len(mylist)))
                if pos.isdecimal():
                    pos = int(pos)
                    if 0 < pos < (len(mylist) + 1):
                        pos -= 1
                        break
                    else:
                        print("bitte nur zahlen von 1 bis " + str(len(mylist)))
                else:
                    print("Bitte nur Zahlen")
            mylist.insert(pos, append)
            print(mylist)
        elif selection == "d":
            sdel = input("Was möchten sie Löschen:")
            try:
                mylist.remove(sdel)
            except ValueError:
                print("Element in liste nicht gefunden")
            print(mylist)
        elif selection == "e":
            seek = input("nach was wollen sie suchen:")
            if seek in mylist:
                print(seek + " ist in der Liste.")
            else:
                print(seek + " ist NICHT in der Liste.")
    else:
        m2list = []
        for i in reversed(mylist):
            m2list.append(i)
        print(m2list)
        break
