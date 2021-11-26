import time


h = int(input("Stunden:"))
m = int(input("Minuten:"))
s = int(input("Sekunden:"))

while True:
    if not(s == 0):
        s -= 1
        '''if len(str(h)) == 1:
            hh = "0" + str(h)
        if len(str(m)) == 1:
            mm = "0" + str(m)
        if len(str(s)) == 1:
            ss = "0" + str(s)'''
        print(f"{h}:{m}:{s}")
        time.sleep(1)
        if s == 0:
            if m > 0:
                s = 60
            else:
                print("--- End ---")
            if not(m == 0):
                m -= 1
                if m == 0:
                    if h > 0:
                        m = 59
                    if not(h == 0):
                        h -= 1
                        if h == 0:
                            h = 0
