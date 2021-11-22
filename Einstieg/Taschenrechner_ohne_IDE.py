number_1 = int(input("Erste Zahl:"))
number_2 = int(input("Zweite Zahl:"))
operator = input("Rechenzeichen:")


if operator == "+":
	print(number_1 + number_2)
	
elif operator == "-":
	print(number_1 - number_2)

elif operator == "*":
	print(number_1 * number_2)

elif operator == "/":
	if number_1 == 0 or number_2 == 0:
		print("Du kannst nicht durch 0 Teilen")
	else:
		print(number_1 / number_2)

elif operator == "//":
	if number_1 == 0 or number_2 == 0:
		print("Du kannst nicht durch 0 Teilen")
	else:
		print(number_1 // number_2)

elif operator == "%":
	print(number_1 % number_2)

else:
	print('Bitte benutze einer der 4 grund operatoren "+ - * /"')
