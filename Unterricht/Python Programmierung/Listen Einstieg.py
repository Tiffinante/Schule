print("Aufgabe 1")
mylist = [345, 73, 4]
print(mylist)
print(len(mylist))
print("Aufgabe 2")
print(mylist[0])
print(mylist[1])
print(mylist[2])
print("Aufgabe 3")
for n in mylist:
    print(n)
print("Aufgabe 4")
for i in range(len(mylist)):
    print(mylist[i])
print("Aufgabe 5")
for i in range(len(mylist) - 1, -1, -1):
    print(mylist[i])
print("Aufgabe 6")
mylist = [345, 834, 73, 45, 4]
total = 0
for n in mylist:
    total += n
print(total)
print("Aufgabe 7")
mylist = []
for i in range(1, 9):
    mylist.append(i**2)
print(mylist)
print("Aufgabe 8")
mylist = [234, "Hallo", 34.34]
m2list = ["popo", True, 5 + 3]
print(mylist, m2list)
mylist.extend(m2list)
print(mylist)
print("Aufgabe 9")
mylist.append(m2list)
print(mylist)
print("Aufgabe 10")
mylist = [123, "huhu", True, 324.34, False]
print(mylist)
mylist.remove(mylist[2])
# mylist.remove(True)
print(mylist)
