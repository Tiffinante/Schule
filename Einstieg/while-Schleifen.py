print("Aufgabe 1")
x = 0
while x != 6:
    print(x, end=" ")
    x += 1

print("\n\nAufgabe 2")
x = 2
while x != 8:
    print(x, end=" ")
    x += 1

print("\n\nAufgabe 3")
x = 1
while x < 20:
    print(x, end=" ")
    x += 2

print("\n\nAufgabe 4")
x = 10
while x > -12:
    print(x, end=" ")
    x -= 2

print("\n\nAufgabe 5")
x = 0   # bis 5
y = 1   # bis 3
while y != 4:
    x = 1
    while x != 6:
        print(y * x, end=" ")
        x += 1
    print("")
    y += 1

print("\n\nAufgabe 6")
number = 7

print('mögliche eingabem: "", "stop" und jede mögliche zahl!')

while number != "" and number != "stop":
    number = input("Number:")

    if number == "stop":
        quit("Programm wird beebdet... (0)")

    if number == "":
        quit("Programm wird beebdet... (1)")

    if number.isdecimal():
        number = int(number)
        if number % 7 == 0:
            print(number, "ist durch 7 Teielbar!")
        else:
            print(number, "ist NICHT durch 7 Teielbar!")
    else:
        print("Bitte nur Zahlen!!!")

quit("Programm wurde beebdet... (2)")
