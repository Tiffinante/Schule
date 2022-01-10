import math

print('''1. Aufgabe: Pi''')
i = 0
n = 1
for k in range(n+1):
    i += (-1)**k / (2 * k + 1)
print(i)
print(math.pi/4)

print('''2. Aufgabe: Schachbrett''')
