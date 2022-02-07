import random

cards = []

for color in range(1, 4+1):
    if color == 1:
        farbe = "Caro"
    elif color == 2:
        farbe = "Pik"
    elif color == 3:
        farbe = "Hetz"
    elif color == 4:
        farbe = "Kreuz"
    else:
        farbe = "fehler"

    for number in range(1, 8+1):
        if number == 1:
            wert = "Ass"
        elif number == 2:
            wert = "König"
        elif number == 3:
            wert = "Dame"
        elif number == 4:
            wert = "Bube"
        elif number == 5:
            wert = "Zehn"
        elif number == 6:
            wert = "Neun"
        elif number == 7:
            wert = "Acht"
        elif number == 8:
            wert = "Sieben"
        else:
            wert = "fehler"
        card = (farbe, wert)
        cards.append(card)

print(len(cards))
print(cards)
# random.shuffle(cards)
"""counter = 0
while counter != 10:
    counter += 1
    while True:
        print("\nTauschen (0 bis 31)")
        try:
            first = int(input("erste karte"))
            second = int(input("zweite  karte"))
        except ValueError:
            print("Bitte nur Zahlen\n")
            first = 0
            second = 0
        if 0 <= first <= 31 and 0 <= second <= 31:
            break
        else:
            print("Bitte nur Zahlen zwischen 0 bis 31\n")
    if first != second:
        cards[first], cards[second] = cards[second], cards[first]
        print(f"({counter} / 10)\n")
    print(cards)
"""
for i in range(100):
    zufallszahl = random.randint(1, 32)
    zufallszahl2 = random.randint(1, 32)
    cards[zufallszahl], cards[zufallszahl2] = cards[zufallszahl2], cards[zufallszahl]

print(cards)