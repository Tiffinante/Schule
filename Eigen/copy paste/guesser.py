from random import randrange
n = randrange(1000)
print('Guess the Number between 0 and 1000!')
while True:
    v = int(input('Number:'))
    if n == v:
        print('You Win!')
        break
    print('Smaller' if (n < v) else 'Bigger')