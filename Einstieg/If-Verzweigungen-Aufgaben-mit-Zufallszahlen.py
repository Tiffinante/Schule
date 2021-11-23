import random


print("Aufgabe 1")
a = random.randint(1, 10)
b = random.randint(1, 10)
if a > b:
    print(a)
    print(b)
else:
    print(b)
    print(a)

print("Aufgabe 2")
a = random.randint(1, 10)
b = random.randint(1, 10)
if a > b:
    print("Zahl1:", a)
    print("Zahl2:", b)
    print("Zahl3:", a - b)
else:
    print("Zahl1:", b)
    print("Zahl2:", a)
    print("Zahl3:", b - a)

print("Aufgabe 3")
a = random.randint(1, 10)
b = random.randint(1, 10)
operator = random.randint(1, 4)
if operator == 1:
    c = a + b
    operator = '+'
elif operator == 2:
    c = a - b
    operator = '-'
elif operator == 3:
    c = a * b
    operator = '*'
elif operator == 4:
    c = a / b
    operator = '/'

if a > b:
    print("Zahl1:", a)
    print("Zahl2:", b)
    print("Zahl3:", c)
else:
    print("Zahl1:", b)
    print("Zahl2:", a)
    print("Zahl3:", operator, c)

print("Aufgabe 3")
print(f'{a} {operator} {b} ergibt {c}')
