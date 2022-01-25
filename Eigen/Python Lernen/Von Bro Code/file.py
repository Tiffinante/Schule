import os
import shutil

from mylibrary import ColorCodes

# \ -> \\
path = "H:\\Neues Textdokument.txt"
print(path)
print("")

# existirt der pfad
if os.path.exists(path):
    print("The location exists")
    #ist es eine datei
    if os.path.isfile(path):
        print("it is a file")
        # Datei öffnen
        try:
            # Schliest die datei automatisch wieder aber
            with open(path) as file:
                print(ColorCodes.BLUE + file.read() + ColorCodes.RESET)
        except FileNotFoundError:
            print("That file was not Found!")
        # datei erstellen oder datei mit dem namen nemen und überschreiben / dazu schreiben
        with open('file.txt', 'w') as file:
            txt = "\nMika Kattau\n2004\nBremen"
            file.write(txt)
        with open('file append or write.txt', 'a') as file:
            list = ["Apfel", "Bananen", "Kirschen", "Mangos", "Ananas"]
            for thing in list:
                txt = thing + "\n"
                file.write(txt)
    else:
        print("it is a folder")
else:
    print("The location dosn't exists")

# copyfile() = copies contents of a file
# copy()     = copyfile() + permission mode + destination can be a directory
# copy2()    = copy() + copies metadata (file's creation and modification times)

# ort und zielort + Neuer name
# shutil.copyfile('file append or write.txt', 'C:\\Users\\katta\\Desktop\\file append or write.txt' )
# shutil.copy('file append or write.txt', 'C:\\Users\\katta\\Desktop\\file append or write.txt' )
# shutil.copy2('file append or write.txt', 'C:\\Users\\katta\\Desktop\\file append or write.txt' )

# Datein verschieben
'''
scr = 'C:\\Users\\katta\\Desktop\\All\\Memes'# source
dst = 'C:\\Users\\katta\\Desktop\\Memes'# destination

try:
    if os.path.exists(dst):
        print("file already exists")
    else:
        os.replace(scr, dst)
        print(scr + " was moved to\n" + dst)
except FileNotFoundError:
    print(scr + " was not found")

path = 'C:\\Users\\katta\\Desktop\\test.txt'

# Datei Löschen
try:
    # Löscht datei
    os.remove(path)

    # Löscht ortner
    # os.rmdir('path')

    # Löscht ortner mit inhalt
    # shutil.rmtree(path)
except FileNotFoundError:
    print("file not found")
except PermissionError:
    print("You do not have permissions to delete that!")
'''