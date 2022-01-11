import os
import time

'''
Wenn eine Datei in einen ordner reingelegt wird,
wird sie automatisch nummereiert 
wenn alse 2 drinne sind heist sie 3
'''

safe_len = 0
path = input('Path:')
old = input("name to rename")

while True:
    old = input("name to rename")
    os.chdir(path)
    len_ordner = len(os.listdir('.'))
    if safe_len == 0:
        safe_len = len_ordner
    if safe_len != len_ordner:
        if safe_len > len_ordner:
            print("Error")
        else:
            time.sleep(0.1)
            safe_len = len_ordner
            os.renames(old, str(len_ordner) + ".png")
