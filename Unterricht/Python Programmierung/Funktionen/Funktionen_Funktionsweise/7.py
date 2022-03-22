# Demonstration mehrerer Parameter 
# Autor: E. Loos

def f( x, y ):
    print( x, " + ", y, " = ", end="")
    x = x + y
    print( x)



# Hauptprogramm
x = 1

f( x, x )
print( "x:", x)
