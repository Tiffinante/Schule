# Goldenerschnitt

max_stelle = int(input("bis stelle:"))
x = 1
print(1, end=" ")
print(1, end=" ")
for i in range(max_stelle - 2):
    x = round(x * 1.618)
    print(x, end=" ")

