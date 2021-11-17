import time


class Car:
    def __init__(self):
        self.car_brand = None
        self.model = None
        self.car_ps = None
        self.color = None


car1 = Car()
car1.car_brand = "BMW"
car1.model = "M4"
car1.car_ps = 250
car1.color = "Red"

car2 = Car()
car2.car_brand = "Audi"
car2.model = "I3"
car2.car_ps = 189
car2.color = "Black"

age = int(input("age:"))
sos = input("Start or Stop")

while True:
    if sos == "Stop" or sos == "stop":
        print("Okay Bye :/")
        break
    elif sos == "Start" or sos == "start":
        print("Lets go")
        break
    else:
        sos = input("Stop or Start:")

if age > 18 or age == 18:
    print("Can we save you login details for the next time?")
    print('at yes or no you can use "i" if mor information')
    savelogin = input('"Yes" or "No"?:')

    while True:
        if savelogin == "i" or savelogin == "I":
            print(" ")
            print("If you agree we will save you full name,")
            print("age, location and sex. we will use your data for")
            print("stats with male and female and about the age.")
            savelogin = input('"Yes" or "No"?:')
        elif savelogin == "Yes" or savelogin == "yes" or savelogin == "y":
            print(" ")
            # save name age por sex
            print("Saving...")
            time.sleep(0.7)
            print("Saving done")
            print(" ")
            break
        elif savelogin == "No" or savelogin == "no" or savelogin == "n":
            print(" ")
            print(":(")
            print("are you sure?")
            sure = input('"Yes" or "No"?:')

            while True:
                if sure == "Yes" or sure == "yes" or sure == "y":
                    print("sadge")
                    break

                elif sure == "No" or sure == "no" or sure == "n":
                    print(" ")
                    print("Can we save you login Data for the next time?")
                    savelogin = input('"Yes" or "No"?:')

                    while True:
                        if savelogin == "Yes" or savelogin == "yes" or savelogin == "y":
                            print(" ")
                            # save name age por sex
                            print("Saving...")
                            time.sleep(0.7)
                            print("Saving done")
                            print(" ")
                            break
                        elif savelogin == "No" or savelogin == "no" or savelogin == "n":
                            print("Sadge")
                            break
                        else:
                            savelogin = input('"Yes" or "No"?:')

                else:
                    savelogin = input('"Yes" or "No"?:')

        else:
            savelogin = input('"Yes" or "No"?:')

else:
    print("You are not 18 years old, so we cannot save your details.")
    print(" ")
