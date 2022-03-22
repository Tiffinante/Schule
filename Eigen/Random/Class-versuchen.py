class Bot:
    # Atrebute
    def __init__(self, age: int, botname = "Bot") -> None:
        self.__name = botname
        self.age = age

    # get Atrebute
    def get_name(self) -> str:
        return self.__name

    def get_age(self) -> int:
        return self.age

    # Methoden/Funktionan
    def roboter_say(self, sting: str) -> None:
        print(self.__name + ": " + sting)

    def __repr__(self) -> str:
        return 'Bot("' + self.__name + '",' + str(self.age) + ')'


mika = Bot(17)
mika.__name = "mika"

david = Bot(botname="David",
            age=16,
            )

print(mika)
print(mika.__repr__())
print(david.__repr__())
mika.roboter_say("Hello")
david.roboter_say("Hello")

print()

mika_str = str(mika)
print(mika_str)
print("Typ von x_str: ", type(mika_str))
neu = eval(mika_str)
print(neu)
print("Typ von neu:", type(neu))

x = A()
x.age = 17
print(x.age)
