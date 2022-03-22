# Demonstration von Einschraenkungen mit globalen Variablen
# Autor: E. Loos

def f():
    x = x + 1
    print( "x:", x)

# Hauptprogramm
x = 1
f()
print( "x:", x)
